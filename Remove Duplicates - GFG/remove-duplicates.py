#User function Template for python3
class Solution:
	def removeDups(self, S):
		# code here
		ans=''
		helper=[0]*26
		for ele in S:
		    helper[ord(ele)-ord('a')]+=1
		for ele in S:
		    if helper[ord(ele)-ord('a')]>0:
		        ans+=ele
		        helper[ord(ele)-ord('a')]=0
		
		
		return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		
		ob = Solution()	
		answer = ob.removeDups(s)
		
		print(answer)


# } Driver Code Ends