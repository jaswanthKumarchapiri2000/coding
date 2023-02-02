#User function Template for python3

class Solution:
    def numberOfPaths (self, n, m):
        # print(a)
        total=n+m-2
        def fact(n):
            ans=1
            for i in range(2,n+1):
                ans*=i
            return ans
        return fact(total)//(fact(n-1) * fact(total-n+1))
        
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