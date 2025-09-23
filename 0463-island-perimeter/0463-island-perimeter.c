int islandPerimeter(int** grid, int gridSize, int* gridColSize) {
    int walls = 0;
    for (int i = 0; i < gridSize; i++) {
        for (int j = 0; j < gridColSize[i]; j++) {
            if (grid[i][j] == 1) {
                walls += 4;
            }
            else continue;
            if ((i+1 < gridSize) && (grid[i+1][j])) {
                walls--;
            }
            if ((i-1 >= 0) && (grid[i-1][j])) {
                walls--;
            }
            if ((j+1 < gridColSize[i]) && (grid[i][j+1])) {
                walls--;
            }
            if ((j-1 >= 0) && (grid[i][j-1])) {
                walls--;
            }
        }     
    }
    return walls;
}