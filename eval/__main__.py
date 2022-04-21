import argparse
import signal
import sys

from eval.evaluator import evaluate


def main():
    arg_parser = argparse.ArgumentParser(
        prog="eval", usage="%(prog)s [expression] [-f FILE] [-h]"
    )
    arg_parser.add_argument(
        "-f",
        action="store",
        dest="file",
        type=str,
        help="the file that stores expressions",
    )
    all_args, others = arg_parser.parse_known_args()
    if all_args.file:
        with open(all_args.file) as f:
            for line in f:
                result = evaluate(line)
                print(result)
    elif len(sys.argv) > 1:
        try:
            user_input = "".join(others)
            value = evaluate(user_input)
            print(value)
        except Exception as e:
            print(e)
            exit(-1)
    else:
        while True:
            try:
                user_input = input("eval > ")
                value = evaluate(user_input)
                print(value)
            except Exception as e:
                print(e)


if __name__ == "__main__":

    def int_handler(sig, frame):
        print("Bye bye!")
        sys.exit(0)

    signal.signal(signal.SIGINT, int_handler)
    main()
