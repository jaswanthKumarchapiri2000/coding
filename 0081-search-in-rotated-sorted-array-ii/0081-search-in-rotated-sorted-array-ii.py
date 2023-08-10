class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low=0
        high=len(nums)-1
        while(low <= high):
            mid=(low+high)//2
            if nums[mid]== target:
                return True
            if nums[low]==nums[mid]:
                low=low+1
                continue
            if nums[mid] == nums[high]:
                high=high-1
                continue
            if nums[low] < nums[mid]:
                if nums[low]<=target<nums[mid] :
                    high=mid-1
                else:
                    low=mid+1
            else:
                if nums[mid] < target <= nums[high]:
                    low=mid+1
                else:
                    high=mid-1
        return False
