#User function Template for python3
class Solution:
    
    def numberOfPaths(self, m, n):
        res1,res2,res3=1,1,1
        for i in range(1,n+m-1):
            res1=res1*i
            if i<=m-1:
                res2=res2*i
            if i <= n-1 :
                res3=res3*i
        return (res1//(res2*res3))% 1000000007



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		m,n = input().split()
		m=int(m)
		n=int(n)
		ob = Solution();
		print(ob.numberOfPaths(m,n))

# } Driver Code Ends