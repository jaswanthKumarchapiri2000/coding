from typing import List


class Solution:
    def dominantPairs(self, n : int, arr : List[int]) -> int:
        # code here
        left_part=arr[:n//2]#we divide arr in two parts left and right
        right_part=arr[n//2:]
        left_part.sort()#sort the left and right parts so we can efficently find suitable pairs
        right_part.sort()
        right=0
        ans=0#intialising the ans 
        for left in range(n//2):
            while right<n//2 and left_part[left]>=5*right_part[right]:
                right+=1
            ans+=right#right is the number with which left index elements forms valid pairs
        return ans
        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.dominantPairs(n, arr)
        
        print(res)
        

# } Driver Code Ends