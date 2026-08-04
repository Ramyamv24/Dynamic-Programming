from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0

        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * cols
        dp[0] = 1

        for r in range(rows):
            for c in range(cols):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                else:
                    if c > 0:
                        dp[c] += dp[c - 1]

        return dp[cols - 1]


# Main Function
if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    obstacleGrid = []
    print("Enter the grid (0 for empty cell, 1 for obstacle):")
    for _ in range(rows):
        obstacleGrid.append(list(map(int, input().split())))

    sol = Solution()
    print("Unique Paths:", sol.uniquePathsWithObstacles(obstacleGrid))