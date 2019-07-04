#!/gridin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function gridelow.
def cavityMap(grid):
    n=len(grid)
    if n==1:
        return grid
    print(grid)
    for i in range(n):
        grid[i]=list(grid[i])
    print(grid)
    for i in range(1,n-1):
        for j in range(1,n-1):
            print(n,i,j)
            if grid[i][j]>grid[i-1][j]:
                if grid[i][j]>grid[i+1][j]:
                    if grid[i][j]>grid[i][j-1]:
                        if grid[i][j]>grid[i][j+1]:
                            grid[i][j]='X'
    for i in range(n):
        grid[i]=''.join(map(str,grid[i]))
    return grid


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
