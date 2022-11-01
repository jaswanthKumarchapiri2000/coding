class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ans=[-1]*len(grid[0])
        for k in range(len(grid[0])):
            i=0
            j=k
            while(0<=j<=len(grid[0])):
                if i==len(grid):
                    ans[k]=j
                    break
                if j==len(grid[0])-1 and grid[i][j]==1:
                    break
                if grid[i][j]==1 :
                    if grid[i][j+1]==1:
                        i+=1
                        j+=1
                    else:
                        break
                else:
                    if grid[i][j-1]==-1:
                        i+=1
                        j-=1
                    else:
                        break
        return ans
                
                
                    
                
        