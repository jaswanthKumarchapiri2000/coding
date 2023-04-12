#User function Template for python3

class Solution():
    def solve(self, a, b, c):
        #your code goes here
        if a >= b and a >=c :
            maxi=a
            other=b+c
        elif b >= c and  b>= a:
            maxi=b
            other=a+c
        elif c >=a and c >= b:
            maxi=c
            other=a+b
        if maxi > 2 *(other+1):
            return -1
        else:
            return sum([a,b,c])


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import Counter
for _ in range(int(input())):
    a, b, c=map(int,input().split())
    obj = Solution()
    res = obj.solve(a, b, c)
    
    print(res)
# } Driver Code Ends