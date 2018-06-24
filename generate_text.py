from argparse import ArgumentParser
import markovify
import lib


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-m', '--model', dest='model', type=str, required=False,
                        help='Model path', default='model.txt')

    args = parser.parse_args()

    print('*' * 50)
    for i in vars(args):
        print(str(i) + ' - ' + str(getattr(args, i)))

    print('*' * 50)

    model_data = lib.read_file(args.model)
    model = markovify.Text.from_json(model_data)
    for _ in range(5):
        while True:
            sentence = model.make_sentence(tries=100, max_overlap_ratio=0.45, max_words=20)
            if sentence:
                break
        print(sentence)