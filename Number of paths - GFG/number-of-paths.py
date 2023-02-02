#User function Template for python3

class Solution:
    def numberOfPaths (self, n, m):
        ans=[[0]*n for i in range(m)]
        ans[0][0]=1
        for i in range(m):
            for j in range(n):
                if i-1>=0 :
                    ans[i][j]+=ans[i-1][j]
                if j-1>=0:
                    ans[i][j]+=ans[i][j-1]
        return ans[m-1][n-1]
        
       
        
        # code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3

        

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        m, n = map(int, input().split())
        ans = ob.numberOfPaths(m, n)
        print(ans)




# } Driver Code Ends