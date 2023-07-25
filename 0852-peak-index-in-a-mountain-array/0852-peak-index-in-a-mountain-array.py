class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        flag=False
        n=len(arr)
        for i in range(n):
            # print(i,flag)
            if not flag and arr[i] > arr[i+1]:
                return i
#             if flag:
#                 if arr[i] > arr[i-1]:
#                     return 0
#         return 1
                
        