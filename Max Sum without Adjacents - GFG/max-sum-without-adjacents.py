#User function Template for python3
class Solution:
	
	def findMaxSum(self,arr, n):
	    ans=[0]*n
	    maxi=0
	    for i in range(n):
	        if i >= 2 :
	            maxi=max(maxi,ans[i-2])
	        else:
	            maxi=0
	            
	        ans[i]=maxi+arr[i]
		# code here
		return max(ans)


#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends