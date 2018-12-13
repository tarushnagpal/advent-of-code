import re
import hashlib
from sys import stderr, argv
from itertools import permutations, combinations, chain, cycle
from functools import reduce as cache
from collections import Counter, deque


# Debug print (to stderr).
def log(*args, **kwargs):
    # kwargs['file'] = stderp
    x = 5

def set_map(f, s):
    return set(map(f, s))

def list_map(f, s):
    return list(map(f, s))

def md5(s):
    return hashlib.md5(bytes(s, 'UTF-8'))

def md5_digest(s):
    return md5(s).hexdigest()

################################################################################

def move(cart, direction, state, tracks):
    x, y = cart
    track = tracks[y][x]
    if track == '+':
        directions = '^<v>'
        turn = [1, 0, -1][state]
        direction = directions[(turn + directions.index(direction)) % len(directions)]
        state = (state + 1) % 3
    log(cart, track, state, direction)
    dX, dY, direction = {
        '|': {
            '^': (0, -1, direction),
            'v': (0, 1, direction)
        }, '-': {
            '>': (1, 0, direction),
            '<': (-1, 0, direction)
        }, '/': {
            '^': (1, 0, '>'),
            '>': (0, -1, '^'),
            'v': (-1, 0, '<'),
            '<': (0, 1, 'v')
        }, '\\': {
            '^': (-1, 0, '<'),
            '<': (0, -1, '^'),
            'v': (1, 0, '>'),
            '>': (0, 1, 'v')
        }, '+': {
            '^': (0, -1, direction),
            '>': (1, 0, direction),
            'v': (0, 1, direction),
            '<': (-1, 0, direction)
        }
    }[track][direction]
    return (x + dX, y + dY), direction, state

def problem1(STRING, LINES):
    directions = {
        '^': '|',
        'v': '|',
        '>': '-',
        '<': '-'
    }

    carts = set()
    cart_directions = {}
    cart_states = {}

    track = []

    y = 0
    for l in LINES:
        track.append([])
        for x, d in enumerate(l):
            if d in directions:
                carts.add((x, y))
                cart_directions[(x, y)] = d
                cart_states[(x, y)] = 0
                track[y].append(directions[d])
            else:
                track[y].append(d)
        y += 1

    first_crash = None
    while True:
        new_carts = set()
        new_cart_directions = {}
        new_cart_states = {}
        carts = sorted(carts, key = lambda t: (t[1], t[0]), reverse=True)
        while carts:
            cart = carts.pop()
            direction = cart_directions[cart]
            state = cart_states[cart]
            new_cart, new_direction, new_state = move(cart, direction, state, track)
            if new_cart not in carts and new_cart not in new_carts:
                new_carts.add(new_cart)
                new_cart_directions[new_cart] = new_direction
                new_cart_states[new_cart] = new_state
            else:
                first_crash = first_crash or new_cart
                new_carts.discard(new_cart)
                if new_cart in carts:
                    carts.remove(new_cart)
                if new_cart in new_cart_directions:
                    del new_cart_directions[new_cart]
                if new_cart in new_cart_states:
                    del new_cart_states[new_cart]
            new_carts.add(new_cart)
            new_cart_directions[new_cart] = new_direction
            new_cart_states[new_cart] = new_state
        carts, cart_directions, cart_states = new_carts, new_cart_directions, new_cart_states
        if len(carts) == 1:
            return first_crash, carts.pop()
        log('new round')

################################################################################

def problem2(STRING, LINES):
    return None

################################################################################

def parse_input_file(fname):
    s = open(fname).read()
    if s and s[-1] == '\n':
        s = s[:-1]
    l = s.splitlines()
    return s, l

def main():
    if len(argv) >= 2 and argv[1] == '-d':
        fname = 'sample.txt'
    else:
        fname = 'files/day_13_input.txt'
    s, l = parse_input_file(fname)
    print(problem1(s, l))
    sol2 = problem2(s, l)
    if sol2 is not None:
        print(sol2)

if __name__ == '__main__':
    main()