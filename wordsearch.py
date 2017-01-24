#!/usr/bin/env python
import click

from random import choice
from string import ascii_lowercase


def load_words():
    with open('words.txt', 'r') as f:
        return set(x.strip().lower() for x in f.readlines())


def generate_grid(size):
    grid = list()
    for _ in range(size):
        row = list()
        for _ in range(size):
            row.append(choice(ascii_lowercase))
        grid.append(row)
    return grid


def display_grid(grid):
    click.echo(grid)

def find_words(grid, valid_words):
    pass


@click.command()
@click.argument('size', default=12)
@click.option('--min-length', '-n', default=0)
def search(size, min_length):
    valid_words = load_words()
    click.echo('Wordlist contains {} valid words.'.format(len(valid_words)))
    grid = generate_grid(size)
    display_grid(grid)
    found = find_words(grid, valid_words)

    if found:
        click.echo('Found {} words: \n{}'.format(
            len(found), '\n'.join(found)))
    else:
        click.echo('No words found.')


if __name__ == '__main__':
    search()
