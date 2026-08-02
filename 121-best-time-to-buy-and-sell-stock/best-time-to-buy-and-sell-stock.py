class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        min_buy= prices[0]
        for i in range(len(prices)):
            if prices[i] < min_buy:
                min_buy=prices[i]
            else:
                profit = prices[i] - min_buy
                if profit > max_profit:
                    max_profit = profit
        return max_profit
        