with open('files/day_11_input.txt') as f:
    serial = int(f.read().strip())
import numpy


def power(x, y):
    rack = (x + 1) + 10
    power = rack * (y + 1)
    power += serial
    power *= rack
    return (power // 100 % 10) - 5

grid = numpy.fromfunction(power, (300, 300))

for width in range(3, 300):
    windows = sum(grid[x:x-width, y:y-width] for x in range(width) for y in range(width))
    maximum = int(windows.max())
    location = numpy.where(windows == maximum)
    print(width, maximum, location[0][0] + 1, location[1][0] + 1)