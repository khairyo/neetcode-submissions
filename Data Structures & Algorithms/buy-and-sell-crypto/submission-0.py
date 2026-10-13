class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # given today, what is the cheapest price i couldve bought before today? at the same time, track the biggest profit so far
        min_price = prices[0]
        best = 0

        for p in prices:
            if p < min_price: 
                min_price = p
            best = max(best, p - min_price)
        return best