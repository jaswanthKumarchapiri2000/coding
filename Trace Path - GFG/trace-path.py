#User function Template for python3

class Solution:
    def isPossible(self, n, m, s):
        # code here]]
        row,col=0,0
        mincol,maxcol=0,0
        minrow,maxrow=0,0
        for ele in s:
            if ele=="L" :
                col-=1
                mincol=min(mincol,col)
                
                if abs(maxcol-mincol)>m-1:
                    return 0
            elif ele=='R':
                col+=1
                maxcol=max(maxcol,col)
                if abs(maxcol-mincol) > m-1 :
                    return 0
            elif ele=='U':
                row-=1
                minrow=min(minrow,row)
                if abs(maxrow-minrow) >= n:
                    return 0
            else:
                row+=1
                maxrow=max(maxrow,row)
                if abs(maxrow-minrow) >=n:
                    return 0
        return 1
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        s = input()
        
        ob = Solution()
        print(ob.isPossible(n, m, s))
# } Driver Code Ends