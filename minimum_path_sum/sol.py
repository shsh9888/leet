class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)  # rows
        n = len(grid[0])  # coums

        if m is 1:
            sum = 0
            for i in range(n):
                sum += grid[0][i]
            return sum

        if n is 1:
            sum = 0
            for i in range(m):
                sum += grid[i][0]
            return sum

        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]

        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        # print(grid)

        return grid[m - 1][n - 1]