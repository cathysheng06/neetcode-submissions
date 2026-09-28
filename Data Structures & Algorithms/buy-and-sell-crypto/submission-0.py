class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = -1
        for i in range(len(prices)): #buy price
            buyPrice=prices[i]
            sellPrice = buyPrice
            maxSell=buyPrice
            for j in range(i+1,len(prices)): #sell prices
                sellPrice = prices[j]
                if(sellPrice>buyPrice and sellPrice>maxSell):
                    maxSell=sellPrice
            if(maxSell-buyPrice > maxProfit):
                maxProfit = maxSell-buyPrice
        return maxProfit


                    
        