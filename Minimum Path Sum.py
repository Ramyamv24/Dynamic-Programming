from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Update first column
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]

        # Update first row
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]

        # Update remaining cells
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]


# Main function
if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    grid = []
    print("Enter the grid values row by row:")

    for _ in range(rows):
        row = list(map(int, input().split()))
        grid.append(row)

    sol = Solution()
    result = sol.minPathSum(grid)

    print("Minimum Path Sum:", result)