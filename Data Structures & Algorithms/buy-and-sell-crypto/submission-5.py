class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        best = 0

        for p in prices:
            if p < min_price:
                min_price = p
            else:
                best = max(best, p - min_price)
        return best