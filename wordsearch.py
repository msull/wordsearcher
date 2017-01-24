#!/usr/bin/env python
import click

from random import choice
from string import ascii_lowercase


def load_words():
    pass

def generate_grid(size):
    pass

def find_words(grid, valid_words):
    pass

@click.command()
@click.argument('size', default=12)
@click.option('--min-length', '-n', default=0)
def search(size, min_length):
    valid_words = load_words()
    grid = generate_grid(size)
    found = find_words(grid, valid_words)

    if found:
        click.echo('Found {} words: \n{}'.format(
            len(found), '\n'.join(found)))
    else:
        click.echo('No words found.')


if __name__ == '__main__':
    search()
