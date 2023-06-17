from collections import defaultdict
class Solution:
	def topK(self, nums, k):
		#Code here
		ret=[]
		d=defaultdict(int)
		for ele in nums:
		    d[ele]+=1
		ans=[]
		for keys in d.keys():
		    ans.append([keys,d[keys]])
		ans.sort(key = lambda x : (x[1],x[0]) ,reverse=True)
		for i in range(k):
		    ret.append(ans[i][0])
		return ret
		    
		    
		    


#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	a = list(map(int, input().strip().split()))
    	n = a[0]
    	nums = a[1:]
    	k = int(input().strip())
    	obj = Solution()
    	ans = obj.topK(nums, k)
    	for i in ans:
    		print(i, end = " ")
    	print()
# } Driver Code Ends