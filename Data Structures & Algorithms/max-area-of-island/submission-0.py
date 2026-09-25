class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # iterate through the matrix/2d array
        # find islands
        # of those islands find the one with the max area
        # once find first land, run dfs, adding area each time a 1 is found
        # once 1 is found, mark as seen in grid by changing val to zero?
        # else keep track of seen
        # everytime new island is found calculate max of new area curr max

        maxArea = 0
        currArea = 0

        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        
        def dfs(r, c):
            nonlocal currArea
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0):
                return
            
            currArea += 1
            grid[r][c] = 0
            for d in directions:
                dfs(r + d[0], c + d[1])

            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    # mark seen
                    dfs(r, c)
                    maxArea = max(maxArea, currArea)
                    currArea = 0

        return maxArea

