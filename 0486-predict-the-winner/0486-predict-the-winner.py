from functools import cache
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n=len(nums)
        dp=[[0 for i in range(n+1)] for j in range(n+1)]
        for i in range(n):
            for j in range(n-i):
                # print(j,j+i, end= " here   ")
                dp[j][j+i]=max(nums[j]-dp[j+1][j+i],nums[j+i]-dp[j][j+i-1])
            # print(dp)
        # print(dp)
        return dp[0][n-1]>=0
                        

            
        