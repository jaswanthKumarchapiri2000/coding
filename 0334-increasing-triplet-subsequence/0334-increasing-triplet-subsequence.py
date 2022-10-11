class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n=len(nums)
        low,medium,high=1e11,1e11,1e11
        for i in nums:
            if i < low:
                low=i
            elif i > low and i < medium :
                medium=i
            elif i > medium :
                high=i
        #print(low,medium,high)
        if high!=1e11 and high > medium:
            return True
        return False
            
            
        