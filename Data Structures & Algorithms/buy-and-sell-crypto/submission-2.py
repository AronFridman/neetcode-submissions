class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxProfit = 0
        while r < len(prices):
            currPrice = prices[l]
            nextPrice = prices[r]
            currProfit = nextPrice-currPrice
            maxProfit = max(maxProfit,currProfit)
            if nextPrice < currPrice:
                l = r
            r+=1
        return maxProfit
            