def maxProfit(prices):
    minPrice = float('inf')
    maxProfit = 0
    
    for i in prices:
        if(prices < minPrice):
            minPrice = prices
        curProfit = prices - minPrice
        if(curProfit > maxProfit):
            maxProfit = curProfit
        
    
    return maxProfit
    
        

print(maxProfit([10,1,5,6,7,1]))
