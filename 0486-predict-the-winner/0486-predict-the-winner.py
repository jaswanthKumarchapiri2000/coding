class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        total=sum(nums)
        n=len(nums)

        def dfs(start,end):
            if start > end:
                # print(start,end,score1,score2)
                return 0
            score1=max(nums[start]-dfs(start+1,end),nums[end]- dfs(start,end-1))
            return score1
             
        if dfs(0,n-1)>=0:
            return True
        return False
        
            
                        

            
        