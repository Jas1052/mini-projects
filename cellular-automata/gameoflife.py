""" John Conway's Game of Life"""
"""
1. Any live cell with fewer than two live neighbors dies (Underpopulation)
2. Any live cell with two or three live neighbors lives on to the next generation
3. Any live cell with three or more neighbors dies (Overpopulation)
4. Any dead cell with exactly three live cells becomes a live cell (Reproduction)
"""
import sys
import time


GLIDER = {
    (2, 2),
    (1, 2),
    (0, 2),
    (2, 1),
    (1, 0),
}

StartCoords = {
	(4, 6),
	(4, 7),
	(4, 8)
}

def neighbors(cell, distance=1):
    """Return the neighbors of cell."""
    x, y = cell
    r = xrange(0 - distance, 1 + distance)
    return ((x + i, y + j) # new cell offset from center
            for i in r for j in r # iterate over range in 2d
            if not i == j == 0) # exclude the center cell


def advance(board):
    """Advance the board one step and return it."""
    new_board = set()
    for cell in board:
        cell_neighbors = set(neighbors(cell))
        # test if live cell dies
        if len(board & cell_neighbors) in [2, 3]:
            new_board.add(cell)
        # test dead neighbors to see if alive
        for n in cell_neighbors:
            if len(board & set(neighbors(n))) is 3:
                new_board.add(n)
    return new_board


def print_board(board, size=None):
    sizex = sizey = size or 0
    for x, y in board:
        sizex = x if x > sizex else sizex
        sizey = y if y > sizey else sizey
    for i in xrange(sizex + 1):
        for j in xrange(sizey + 1):
            sys.stdout.write(' x ' if (i, j) in board else ' . ')
        print


def constrain(board, size):
    return set(cell for cell in board if cell[0] <= size and cell[1] <= size)


def main(board, steps=75, size=20):
    for i in xrange(1, steps + 1):
        sys.stdout.write('\033[H')  # move to the top
        sys.stdout.write('\033[J')  # clear the screen
        print 'step:', i, '/', steps
        print_board(board, size)
        time.sleep(1) # time per stepi
        board = constrain(advance(board), size)


if __name__ == '__main__':
    main(StartCoords)
