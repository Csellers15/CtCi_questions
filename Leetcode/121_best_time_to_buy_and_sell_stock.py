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
      
     #Other Solution Better 
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = sys.maxsize
        
        for price in prices: 
            if minPrice > price:
                minPrice = price 
            elif price - minPrice > maxProfit:
                maxProfit = price - minPrice
            
        return maxProfit
