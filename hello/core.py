import sys


def say_hello(to, file=None):
    if file is None:
        file = sys.stdout
    print('Hello, {}!'.format(to), file=file)
