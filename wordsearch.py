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
    for row in grid:
        click.echo(' '.join(row))


def find_words(search_strs, valid_words):
    found = list()
    for word in valid_words:
        if any(word in x for x in search_strs):
            found.append(word)
    return found


def get_grid_strings(grid):
    """Get the set of all valid strings in the grid.

    > get_grid_strings([['a', 'b'], ['c', 'd']])
    """
    str_fns = (
        _horizontal_strings,
        _vertical_strings,
        _diagonal_down_right_strings,
        _diagonal_down_left_strings,
    )
    return set(sum(map(lambda x: x(grid), str_fns), []))


def _reverse_strs(strs):
    return list([x[::-1] for x in strs])


def _horizontal_strings(grid):
    """Return all horizontal strs, forwards and backwards."""
    strs = list()
    for row in grid:
        strs.append(''.join(row))

    return strs + _reverse_strs(strs)


def _vertical_strings(grid):
    strs = list()
    for col in zip(*grid):
        strs.append(''.join(col))

    return strs + _reverse_strs(strs)


def _diagonal_down_right_strings(grid):
    return []


def _diagonal_down_left_strings(grid):
    return []


@click.command()
@click.argument('size', default=12)
@click.option('--min-length', '-n', default=0)
def search(size, min_length):
    valid_words = load_words()
    click.echo('Wordlist contains {} valid words.'.format(len(valid_words)))
    grid = generate_grid(size)
    display_grid(grid)
    grid_strs = get_grid_strings(grid)
    click.echo(grid_strs)
    found = find_words(grid_strs, valid_words)

    if found:
        click.echo('Found {} words: \n{}'.format(
            len(found), '\n'.join(found)))
    else:
        click.echo('No words found.')


if __name__ == '__main__':
    search()
