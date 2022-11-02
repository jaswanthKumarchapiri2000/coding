from typing import List


from typing import List


class Solution:
    def largestArea(self,n:int,m:int,k:int, enemy : List[List[int]]) -> int:
        row=[1]*n
        col=[1]*m
        for i in range(len(enemy)):
            row[enemy[i][0]-1]=0
            col[enemy[i][1]-1]=0
        maxr,maxc,count=0,0,0
        for i in range(n):
            if row[i]==1:
                count+=1
                maxr=max(maxr,count)
            else:
                count=0
            
        count=0
        for i in range(m):
            if col[i]==1:
                count+=1
                maxc=max(maxc,count)
            else:
                count=0
            
        return maxr*maxc
            
                
        



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



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(3)
        n,m,k=a[0],a[1],a[2]
        
        e=IntMatrix().Input(a[2], 2)
        
        obj = Solution()
        res = obj.largestArea(n,m,k, e)
        
        print(res)
        

# } Driver Code Ends