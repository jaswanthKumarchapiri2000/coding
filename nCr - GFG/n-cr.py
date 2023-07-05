#User function Template for python3
import math
class Solution:
    def nCr(self, n, r):
        # code here
        if n==r:
            return 1
        if n <r:
            return 0
        prev=[1,1]
        cur=[]
        if n==1:
            return 1
        for i in range(2,n+1):
            cur=[]
            cur.append(1)
            for i in range(len(prev)-1):
                ele=prev[i]+prev[i+1]
                cur.append(ele)
            cur.append(1)
            prev=cur
        # print(prev)
        return prev[r] % 1000000007
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.nCr(n, r))
# } Driver Code Ends