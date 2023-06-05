#User function Template for python3

class Solution:
    def AllPossibleStrings(self, s):
        n = len(s)
        ans = []
        
        def dfs(ind, stack, n):
            if ind == n :
                ans.append(stack[:])
            else:
                stack1 = stack + s[ind]
                dfs(ind + 1, stack1, n)
                dfs(ind + 1, stack, n)
        
        dfs(0, "", n)
        ans.remove("")
        ans.sort()
        return ans

		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends