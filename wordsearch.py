#!/usr/bin/env python
import click

from random import choice
from string import ascii_lowercase


def load_words(min_length):
    # add 1 to min_length to account for newling character -- faster than strip
    min_length += 1
    with open('words.txt', 'r') as f:
        return set(x.strip().lower() for x in f.readlines() if len(x) >= min_length)


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
    strs = list()
    size = len(grid)
    center_str = list()
    for x in range(size):
        center_str.append(grid[x][x])
    strs.append(''.join(center_str))

    for x in range(1, size):
        this_str_1 = list()
        this_str_2 = list()
        for y in range(x, size):
            this_str_1.append(grid[y][y - x])
            this_str_2.append(grid[y - x][y])
        strs.append(''.join(this_str_1))
        strs.append(''.join(this_str_2))
    return strs + _reverse_strs(strs)


def _diagonal_down_left_strings(grid):
    # cheat and rotate the grid 90 degrees and find down-right again
    return _diagonal_down_right_strings(zip(*grid[::-1]))


@click.command()
@click.argument('size', default=12)
@click.option('--min-length', '-n', default=0)
def search(size, min_length):
    valid_words = load_words(min_length)
    click.echo('Wordlist contains {} valid words.'.format(len(valid_words)))
    grid = generate_grid(size)
    display_grid(grid)
    grid_strs = get_grid_strings(grid)
    found = find_words(grid_strs, valid_words)

    if found:
        click.echo('Found {} words: \n{}'.format(
            len(found), '\n'.join(found)))
    else:
        click.echo('No words found.')


if __name__ == '__main__':
    search()
