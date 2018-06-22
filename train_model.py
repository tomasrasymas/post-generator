import markovify
from argparse import ArgumentParser
import lib


def train(model_path, corpus_path, state_size=2):
    corpus = lib.read_file(corpus_path)
    text_model = markovify.Text(corpus, state_size=state_size)
    model_json = text_model.to_json()
    lib.write_list_to_file(model_path, [model_json])


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-m', '--model', dest='model', type=str, required=False,
                        help='Generated model path',
                        default='model.txt')
    parser.add_argument('-c', '--corpus', dest='corpus', type=str, required=False,
                        help='Corpus file path', default='corpus.txt')

    args = parser.parse_args()

    print('*' * 50)
    for i in vars(args):
        print(str(i) + ' - ' + str(getattr(args, i)))

    print('*' * 50)

    train(args.model, args.corpus)