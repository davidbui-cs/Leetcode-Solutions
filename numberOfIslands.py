class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numRows = len(grid)
        numCols = len(grid[0])
        num_islands = 0
        for row in range(numRows):
            for col in range(numCols):
                if(grid[row][col] == '1'):
                    self.dfs(grid, row, col)
                    num_islands +=1
        return num_islands
                
    def dfs(self, grid, row, col):
        if( (col > len(grid[0])) or (col < 0) or (row > len(grid)) or (row < 0)):
            return
        
        grid[row][col] = '0'
        if( (col+1 < len(grid[0])) and (grid[row][col+1] == '1')):
            self.dfs(grid, row, col+1)
        if( (col-1 >=0) and (grid[row][col-1] == '1')):
            self.dfs(grid, row, col-1)
        if( (row+1 < len(grid)) and (grid[row+1][col] == '1')):
            self.dfs(grid, row+1, col)
        if( (row-1 >=0) and (grid[row-1][col] == '1')):
            self.dfs(grid, row-1, col)
        