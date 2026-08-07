class Solution:
    def solve(self, l, r, s, dp):
        if r < l:
            return 0

        if dp[l][r] != -1:
            return dp[l][r]

        if s[l] == s[r]:
            if l == r:
                dp[l][r] = 1 + self.solve(l + 1, r - 1, s, dp)
            else:
                dp[l][r] = 2 + self.solve(l + 1, r - 1, s, dp)
        else:
            dp[l][r] = max(
                self.solve(l + 1, r, s, dp),
                self.solve(l, r - 1, s, dp)
            )

        return dp[l][r]

    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[-1] * n for _ in range(n)]
        return self.solve(0, n - 1, s, dp)


# Main part
if __name__ == "__main__":
    s = input("Enter a string: ")

    solution = Solution()
    result = solution.longestPalindromeSubseq(s)

    print("Length of Longest Palindromic Subsequence:", result)