#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        helper=[(i,j) for i,j in zip(start,end)]
        helper.sort()
        helper.sort(key = lambda s : s[1])
        ans=1
        first=helper[0][0]
        second=helper[0][1]
        for i,j in helper[1:]:
            if i > second:
                ans+=1
                second=j
        return ans
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends