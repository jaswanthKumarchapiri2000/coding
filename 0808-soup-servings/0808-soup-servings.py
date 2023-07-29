from functools import cache
from fractions import Fraction
class Solution:
    def soupServings(self, n: int) -> float:
        a=b=n
        if  n > 4275:
            return 1.0
        if n==0:
            return 0.5
        @cache
        def dfs(a,b):
            # print(a,b)
            temp=0.25
            if a <=0 and b <=0:
                return 0.5
            if a <=0 :
                return 1
            if b <=0:
                return 0
            ans=temp*(dfs(a-100,b))
            ans+=temp*(dfs(a-75,b-25))
            ans+=temp*(dfs(a-50,b-50))
            ans+=temp*(dfs(a-25,b-75))
            return ans
            
        return dfs(n,n)
        