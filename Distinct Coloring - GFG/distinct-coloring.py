#User function Template for python3

class Solution:
    def distinctColoring (self, N, r, g, b):
        # code here
        ans=[[ 0 for i in range(3)] for j in range(N)]
        ans[0][0] = r[0]
        ans[0][1]= g[0]
        ans[0][2]= b[0]
        for i in range(1,N):
            ans[i][0]=r[i]+min(ans[i-1][1],ans[i-1][2])
            ans[i][1]=g[i]+min(ans[i-1][0],ans[i-1][2])
            ans[i][2]=b[i]+min(ans[i-1][0],ans[i-1][1])
        return min(ans[N-1])
            
            
            
            
            
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        r = list(map(int, input().split()))
        g = list(map(int, input().split()))
        b = list(map(int, input().split()))

        ob = Solution()
        print(ob.distinctColoring(N, r, g, b))
# } Driver Code Ends