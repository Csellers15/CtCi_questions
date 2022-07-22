    def maxPower(self, s: str) -> int:
        current, maxCount = 0, 0
        previous = None
        
        for c in s: 
            if c == previous:
                current += 1 
            else: 
                previous = c
                current = 1
            
            if(current > maxCount):
                maxCount = current
        
        return maxCount
