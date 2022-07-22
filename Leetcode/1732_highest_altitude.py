    def largestAltitude(self, gain: List[int]) -> int:
        currentAlt, maxAlt = 0, 0
        
        for change in gain:
            currentAlt += change
            
            if(currentAlt > maxAlt):
                maxAlt = currentAlt
                
        return maxAlt
