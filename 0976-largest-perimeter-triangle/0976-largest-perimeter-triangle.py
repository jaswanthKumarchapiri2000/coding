class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n=len(nums)
        for i in range(2,n):
            if nums[i-2]< nums[i-1]+nums[i]:
                return sum(nums[i-2:i+1])
        return 0
            
            
            
        