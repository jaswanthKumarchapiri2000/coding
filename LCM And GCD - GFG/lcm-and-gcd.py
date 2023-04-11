#User function Template for python3

class Solution:
    def lcmAndGcd(self, A , B):
        # code here 
        def gcd(A , B):
            
            if A==0:
                return B
            return gcd(B%A,A)
        ans=[0]*2
        ans[1]=gcd(A,B)
        ans[0]=(A*B)//ans[1]
        return ans
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split())
        
        ob = Solution()
        ptr = ob.lcmAndGcd(A,B)
        
        print(ptr[0],ptr[1])
# } Driver Code Ends