from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0

        dp = [1] * n  # Every element is an LIS of length 1

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


if __name__ == "__main__":
    nums = list(map(int, input("Enter the elements separated by space: ").split()))

    sol = Solution()
    print("Length of Longest Increasing Subsequence:", sol.lengthOfLIS(nums))