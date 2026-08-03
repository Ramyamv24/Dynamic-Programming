class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1  # One way to make 0: choose nothing

        for t in range(1, target + 1):
            for num in nums:
                if num <= t:
                    dp[t] += dp[t - num]

        return dp[target]


def main():
    nums = list(map(int, input("Enter the numbers: ").split()))
    target = int(input("Enter the target: "))

    sol = Solution()
    result = sol.combinationSum4(nums, target)

    print("Number of possible combinations:", result)


if __name__ == "__main__":
    main()