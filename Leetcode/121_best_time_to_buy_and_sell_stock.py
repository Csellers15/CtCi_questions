  #Solution is corretc but is brute force   
  def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        profit = 0
        
        firstPointer = 0 
        secondPointer = 1
        pricesLength = len(prices)
        
        while firstPointer < pricesLength:
            while secondPointer < pricesLength:
                profit = prices[secondPointer] - prices[firstPointer]
                if(profit > maxProfit):
                    maxProfit = profit
                
                secondPointer += 1
            
            firstPointer += 1
            secondPointer = firstPointer + 1
            
        return maxProfit
      
    #NeetCodes Python Solution using 2 pointers 
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        
        l = 0 
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                 l = r
            maxProfit = max(maxProfit, prices[r] - prices[l])
        return maxProfit
      
    #My solution 
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = sys.maxsize
        
        for price in prices: 
            if minPrice > price:
                minPrice = price 
            elif price - minPrice > maxProfit:
                maxProfit = price - minPrice
            
        return maxProfit
     
