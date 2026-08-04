class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        aboveRow = [1] * n

        for _ in range(m - 1):
            currentRow = [1] * n
            for i in range(1, n):
                currentRow[i] = currentRow[i - 1] + aboveRow[i]
            aboveRow = currentRow

        return aboveRow[-1]


# Main function
if __name__ == "__main__":
    m = int(input("Enter number of rows (m): "))
    n = int(input("Enter number of columns (n): "))

    obj = Solution()
    print("Number of unique paths:", obj.uniquePaths(m, n))