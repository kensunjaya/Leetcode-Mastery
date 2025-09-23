class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        walls = 0
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    walls += 4
                else:
                    continue
                if i+1 < rows and grid[i+1][j]:
                    walls -= 1
                if i-1 >= 0 and grid[i-1][j]:
                    walls -= 1
                if j+1 < cols and grid[i][j+1]:
                    walls -=1
                if j-1 >= 0 and grid[i][j-1]:
                    walls -=1
        return walls