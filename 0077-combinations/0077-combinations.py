class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr=[ i+1 for i in range(n)]
        ans=[]
        def dfs(ind,res,count):
            if ind >= n :
                if count > k:
                    return
                elif count < k:
                    return 
                else:
                    ans.append(res[:])
                    return
            if count==k:
                ans.append(res[:])
            else:
                res.append(arr[ind])
                dfs(ind+1,res,count+1)
                res.pop()
                dfs(ind+1,res,count)
        dfs(0,[],0)
        return ans      