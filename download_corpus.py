import lib
from argparse import ArgumentParser
import time
import os


def download_corpus(url, file_path):
    if url:
        buffer = []
        for link, description in lib.download_text(url):
            print(link)
            buffer.append(description.strip() + os.linesep)
            for post_part in lib.parse_post(link):
                buffer.append(post_part.strip() + os.linesep)
                time.sleep(0.5)

        lib.write_list_to_file(file_path, buffer)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-u', '--url', dest='url', type=str, required=False,
                        help='URL of delfi.lt rss item index to generate text file',
                        default='https://www.delfi.lt/rss/feeds/lithuania.xml')
    parser.add_argument('-o', '--output', dest='output', type=str, required=False,
                        help='Path of text file to output downloaded rss index text', default='corpus.txt')

    args = parser.parse_args()

    print('*' * 50)
    for i in vars(args):
        print(str(i) + ' - ' + str(getattr(args, i)))

    print('*' * 50)

    download_corpus(args.url, args.output)