from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dfs(sumi,index):
            nonlocal coins
            n=len(coins)
            if index >= n:
                return 0
            if sumi > amount :
                return 0
            if sumi == amount:
                return 1
            ele=coins[index]
            ans=dfs(sumi+ele,index)
            ans+=dfs(sumi,index+1)
            return ans
        return dfs(0,0)
        