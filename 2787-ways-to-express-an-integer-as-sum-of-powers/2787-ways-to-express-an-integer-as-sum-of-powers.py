from functools import cache
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod=int(1e9+7)
        ele=1
        ans=[]
        while(ele**x) <= n:
            temp=ele**x
            ans.append(temp)
            ele+=1
        ret=0
        print(ans)
        ans_len=len(ans)
        dp=[[0 for i in range(n+1)] for i in range(ans_len+1)]
        for i in range(1,ans_len+1):
            for j in range(1,n+1):
                if j==ans[i-1]:
                    dp[i][j]+=1
                dp[i][j]+=dp[i-1][j]
                if j-ans[i-1] >=0:
                    dp[i][j]+=dp[i-1][j-ans[i-1]]
        # print(dp)
        return dp[ans_len][n] % mod