class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        n = len(prices)

        # hold = max profit while holding a stock
        # sold = max profit after selling today
        # rest = max profit while resting

        hold = -prices[0]
        sold = 0
        rest = 0

        for i in range(1, n):
            prev_hold, prev_sold, prev_rest = hold, sold, rest

            hold = max(prev_hold, prev_rest - prices[i])
            sold = prev_hold + prices[i]
            rest = max(prev_rest, prev_sold)

        return max(sold, rest)


def main():
    n = int(input("Enter number of days: "))

    prices = list(map(int, input("Enter stock prices: ").split()))

    # Check whether the number of prices matches n
    if len(prices) != n:
        print("Please enter exactly", n, "prices.")
        return

    obj = Solution()
    result = obj.maxProfit(prices)

    print("Maximum Profit:", result)


if __name__ == "__main__":
    main()