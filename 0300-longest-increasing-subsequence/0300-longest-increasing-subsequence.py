class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        maxi=1
        arr=[1]*n
        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j] and arr[i]< 1+arr[j]:
                    arr[i]=arr[j]+1
            maxi=max(maxi,arr[i])
        return maxi
        
            
        