# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def binary_search(low,high,target,first):
            
            nonlocal mountain_arr
            if first:
                while True:
                    
                    if high < low:
                        return -1
                    mid=(low+high)//2
                    # print(low,high,mid)
                    if target==mountain_arr.get(mid):
                        return mid
                    elif target > mountain_arr.get(mid):
                        low=mid+1
                    else:
                        high=mid-1
            else:
                while True:
                    # print(low,high,first)
                    if high < low:
                        return -1
                    mid=(low+high)//2
                    # print(low,high,mid)
                    if target==mountain_arr.get(mid):
                        return mid
                    elif target < mountain_arr.get(mid):
                        low=mid+1
                    else:
                        high=mid-1
                
                
        ans=-1
        n=mountain_arr.length()
        left,right=0,n-1
        highest=0
        while(True):
            mid=(left+right)//2
            # print(left,right,mid)
            if mid==0:
                highest=1
                break
            if mid==n-1:
                highest=n-2
                break
            if ((mountain_arr.get(mid) > mountain_arr.get(mid-1)) and(mountain_arr.get(mid)>mountain_arr.get(mid+1))):
                highest=mid
                break
                                                                      
            elif (mountain_arr.get(mid) > mountain_arr.get(mid+1)):
                right=mid-1
            else:
                left=mid+1
        # print(" highest " , highest)
        if target==mountain_arr.get(highest):
            return highest
        if mountain_arr.get(0)<= target <= mountain_arr.get(highest):
            temp=binary_search(0,highest,target,1)
            if temp!=-1:
                return temp
                
        return binary_search(highest+1,n-1,target,0)
        
                                                                      
        