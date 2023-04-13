#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def generateBinaryStrings(self, n):
        # Code here
        ans=[]
        def helper(ans,string,n):
            if n==1:
                ans.append(string)
            else:
                if string[-1]=='0':
                    helper(ans,string+'0',n-1)
                    helper(ans,string+'1',n-1)
                else:
                    helper(ans,string+'0',n-1)
        helper(ans,'0',n)
        helper(ans,'1',n)
        # ans.sort()
        return ans

#{ 
 # Driver Code Starts.
from sys import stdout
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        res = ob.generateBinaryStrings(N)
        for binaryString in res:
            print(binaryString, end = ' ')
        print()
# } Driver Code Ends