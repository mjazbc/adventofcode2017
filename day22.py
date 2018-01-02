import numpy as np
import os
import time

with open('data/' + os.path.basename(__file__).rstrip('.py') + '_input.txt', 'r') as file:
    data = np.matrix([list(line.strip()) for line in file.readlines()])

def rotate(x ,y ,rot, grid):
    grid[y, x] = '*'
    grid = np.rot90(grid, rot)
    y, x = np.where(grid == '*')
    return y,x, grid


def move_virus(grid,x,y,n):
    inf_count = 0
    for _ in range(n):
        if grid[y , x] == '#':
            y,x, grid = rotate(x,y,1,grid)
            grid[y, x] = '.'
        elif grid[y , x] == '.':
            y, x, grid = rotate(x, y, -1, grid)
            grid[y, x] = '#'
            inf_count += 1

        y -= 1 # move up
        # print(grid)
    return inf_count, grid


def move_virus_wf(grid,n):
    inf_count = 0
    x = len(grid)//2
    y = x
    t = time.time()
    for i in range(n):
        if grid[y , x] == '#':
            y,x, grid = rotate(x,y,1,grid)
            grid[y, x] = 'F'
        elif grid[y, x] == 'F':
           y, x, grid = rotate(x, y, 2, grid)
           grid[y, x] = '.'
        elif grid[y , x] == '.':
            y, x, grid = rotate(x, y, -1, grid)
            grid[y, x] = 'W'
        elif grid[y, x] == 'W':
            # y, x, grid = rotate(x, y, 0, grid)
            grid[y, x] = '#'
            inf_count += 1

        if y == 0:
            grid = np.vstack(((np.full((1, grid.shape[1]), '.')), grid, (np.full((1, grid.shape[1]), '.'))))
            y = 1
        if x == 0:
            grid = np.hstack(((np.full((grid.shape[0], 1,), '.')), grid, (np.full((grid.shape[0], 1), '.'))))
            x = 1

        y -= 1 #  move up

        if i % 100000 == 0:
            print(time.time() -t)
            t = time.time()

    return inf_count, grid


# dim = 10
# grid = np.full((dim, dim), '.')
# lower = (dim // 2) - (len(data) // 2)
# upper = (dim // 2) + (len(data) // 2)
grid = data
# print(grid)
# inf_count, tmp = move_virus(grid.copy(), dim//2, dim//2, 100)

t = time.time()
inf_count, tmp = move_virus_wf(grid, 10000000)
print(time.time() -t)

print(tmp)
print(inf_count)
