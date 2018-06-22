import requests
from bs4 import BeautifulSoup
from requests_xml import XMLSession


def write_list_to_file(file_path, data):
    with open(file_path, 'w', encoding='utf8') as f:
        f.writelines(data)


def read_file(file_path):
    with open(file_path, 'r', encoding='utf8') as f:
        corpus = f.read()
        return corpus


def parse_post(url):
    if url:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            body = soup.find('div', {'itemprop': 'articleBody'})
            if body:
                post_parts = body.find_all('p', text=True, recursive=False)
                if post_parts:
                    for post_part in post_parts:
                        yield post_part.text.strip()


def download_text(url):
    if url:
        session = XMLSession()
        try:
            response = session.get(url)
        finally:
            if session:
                session.close()

        if response:
            items = response.xml.xpath('//item')

            for item in items:
                descritpion = item.xpath('//description')[0].text
                link = item.xpath('//link')[0].text
                yield link, descritpion
