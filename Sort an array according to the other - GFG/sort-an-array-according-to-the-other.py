#User function Template for python3
from collections import defaultdict

class Solution:
    # A1[] : the input array-1
    # N : size of the array A1[]
    # A2[] : the input array-2
    # M : size of the array A2[]
    
    #Function to sort an array according to the other array.
    def relativeSort (self,A1, N, A2, M):
        # Your Code Here
        d1=defaultdict(int)
        for ele in A1:
            d1[ele]+=1
        ans=[]
        for key in A2:
            while d1[key] > 0:
                ans.append(key)
                d1[key]-=1
        helper=[]
        for key in d1:
            while(d1[key] > 0):
                helper.append(key)
                d1[key]-=1
        helper.sort()
        ans.extend(helper)
        return ans
        
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int (input ())
    while t > 0:
        n, m = list(map(int, input().split()))
        a1 = list(map(int, input().split()))
        a2 = list(map(int, input().split()))
        
        ob=Solution()
        a1 = ob.relativeSort (a1, n, a2, m)
        print (*a1, end = " ")
        
        print ()
        
        t -= 1

# } Driver Code Ends