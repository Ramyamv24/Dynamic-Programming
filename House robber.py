from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[-1]


if __name__ == "__main__":
    nums = list(map(int, input("Enter house values separated by space: ").split()))

    sol = Solution()
    print("Maximum money that can be robbed:", sol.rob(nums))