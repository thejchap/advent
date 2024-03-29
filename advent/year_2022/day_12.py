"""
--- Day 12: Hill Climbing Algorithm ---
You try contacting the Elves using your handheld device, but the river you're following must be too low to get a decent signal.

You ask the device for a heightmap of the surrounding area (your puzzle input). The heightmap shows the local area from above broken into a grid; the elevation of each square of the grid is given by a single lowercase letter, where a is the lowest elevation, b is the next-lowest, and so on up to the highest elevation, z.

Also included on the heightmap are marks for your current position (S) and the location that should get the best signal (E). Your current position (S) has elevation a, and the location that should get the best signal (E) has elevation z.

You'd like to reach E, but to save energy, you should do it in as few steps as possible. During each step, you can move exactly one square up, down, left, or right. To avoid needing to get out your climbing gear, the elevation of the destination square can be at most one higher than the elevation of your current square; that is, if your current elevation is m, you could step to elevation n, but not to elevation o. (This also means that the elevation of the destination square can be much lower than the elevation of your current square.)

For example:

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
Here, you start in the top-left corner; your goal is near the middle. You could start by moving down or right, but eventually you'll need to head toward the e at the bottom. From there, you can spiral around to the goal:

v..v<<<<
>v.vv<<^
.>vv>E^^
..v>>>^^
..>>>>>^
In the above diagram, the symbols indicate whether the path exits each square moving up (^), down (v), left (<), or right (>). The location that should get the best signal is still E, and . marks unvisited squares.

This path reaches the goal in 31 steps, the fewest possible.

What is the fewest steps required to move from your current position to the location that should get the best signal?

Your puzzle answer was 380.

--- Part Two ---
As you walk up the hill, you suspect that the Elves will want to turn this into a hiking trail. The beginning isn't very scenic, though; perhaps you can find a better starting point.

To maximize exercise while hiking, the trail should start as low as possible: elevation a. The goal is still the square marked E. However, the trail should still be direct, taking the fewest steps to reach its goal. So, you'll need to find the shortest path from any square at elevation a to the square marked E.

Again consider the example from above:

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
Now, there are six choices for starting position (five marked a, plus the square marked S that counts as being at elevation a). If you start at the bottom-left square, you can reach the goal most quickly:

...v<<<<
...vv<<^
...v>E^^
.>v>>>^^
>^>>>>>^
This path reaches the goal in only 29 steps, the fewest possible.

What is the fewest steps required to move starting from any square with elevation a to the location that should get the best signal?

Your puzzle answer was 375.

Both parts of this puzzle are complete! They provide two gold stars: **
"""

from advent.tools import *


def bfs(grid, start, end):
    dist = cl.defaultdict(int)
    q = cl.deque([(0, start)])
    while q:
        d, (r, c) = q.popleft()
        if (r, c) == end:
            return d
        for nr, nc in util.grid_neighbors(r, c, grid):
            if ord(grid[nr][nc]) - ord(grid[r][c]) > 1:
                continue
            if (nr, nc) in dist:
                continue
            nd = d + 1
            dist[(nr, nc)] = nd
            q.append((nd, (nr, nc)))


def extract_start_end(grid):
    start = (-1, -1)
    end = (-1, -1)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "S":
                start = (r, c)
                grid[r][c] = "a"
            elif grid[r][c] == "E":
                end = (r, c)
                grid[r][c] = "z"
    return start, end, grid


def _pt1(grid):
    start, end, grid = extract_start_end(grid)
    return bfs(grid, start, end)


def _pt2(grid):
    _, end, grid = extract_start_end(grid)
    shortest = float("inf")
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != "a":
                continue
            if dist := bfs(grid, (r, c), end):
                shortest = min(shortest, dist)
    return shortest


TEST = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""
ANSWERS = [31, 380, 29, 375]


def main():
    return afs.input_lines(
        tests=[TEST],
        parts=[_pt1, _pt2],
        transform_line=list,
    )
