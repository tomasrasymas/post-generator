import lib
from argparse import ArgumentParser
import time
import os

URL = 'https://www.delfi.lt/rss'


def download_corpus(file_path):
    buffer = []
    for link, description in lib.download_text(URL):
        print(link, description)
        print('*' * 30)
        for sub_link, sub_description in lib.download_text(link):
            print(sub_link)
            buffer.append(sub_description.strip() + os.linesep)
            for post_part in lib.parse_post(sub_link):
                proc_post = post_part.strip()
                if len(proc_post.split()) > 5:
                    buffer.append(proc_post + os.linesep)
                time.sleep(0.5)

    lib.write_list_to_file(file_path, buffer)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-o', '--output', dest='output', type=str, required=False,
                        help='Path of text file to output downloaded rss index text', default='corpus.txt')

    args = parser.parse_args()

    print('*' * 50)
    for i in vars(args):
        print(str(i) + ' - ' + str(getattr(args, i)))

    print('*' * 50)

    download_corpus(args.output)