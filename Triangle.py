from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row = len(triangle)
        memo = triangle[row - 1].copy()

        # Bottom-up DP
        for r in range(row - 2, -1, -1):
            for c in range(r + 1):
                memo[c] = min(memo[c], memo[c + 1]) + triangle[r][c]

        return memo[0]


# Main function
if __name__ == "__main__":
    n = int(input("Enter the number of rows in the triangle: "))

    triangle = []
    print("Enter the triangle values row by row:")

    for i in range(n):
        row = list(map(int, input().split()))
        triangle.append(row)

    sol = Solution()
    result = sol.minimumTotal(triangle)

    print("Minimum Total:", result)