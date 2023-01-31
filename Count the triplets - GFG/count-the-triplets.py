#User function Template for python3
class Solution:
	def countTriplet(self, arr, n):
	    
		# code here
		ans=0
		d={}
		for i in range(n):
		    ele=arr[i]
		    d[ele]=i
		    
		for i in range(n):
		    for j in range(i+1,n):
		        s=arr[i]+arr[j]
		        if s in d:
		            ans+=1
		return ans
		
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		arr = [int(x) for x in input().split()]

		ob = Solution()
		ans = ob.countTriplet(arr, n)
		print(ans)

# } Driver Code Ends