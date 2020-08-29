#!/usr/bin/python
import argparse
import sys
from lib.evaluator import evaluate


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-f", action="store", dest="file", type=str)
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
            exit(-3)
    else:
        while True:
            try:
                user_input = input("eval > ")
                value = evaluate(user_input)
                print(value)
            except Exception as e:
                print(e)
