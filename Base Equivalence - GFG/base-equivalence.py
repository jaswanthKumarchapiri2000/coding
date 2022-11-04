#User function Template for python3
class Solution:
	def baseEquiv(self, n, m):
	    if m==1 and n <=32:
	        return 'Yes'
	    def helper(num,base):
	        s=''
	        while(num!=0):
	            basedigit=num%base
	            if basedigit<10:
	                s=str(basedigit)+s
	            else:
	                k=chr(ord('a')+basedigit-10)
	                s=k+s
	            num=num//base
	        return s
	    for i in range(2,33):
	        if len(helper(n,i))==m:
	            return 'Yes'
	    return 'No'



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,m = input().split()
		n=int(n)
		m=int(m)
		ob = Solution();
		print(ob.baseEquiv(n,m))

# } Driver Code Ends