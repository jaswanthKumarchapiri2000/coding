#User function Template for python3

class Solution:

    def findMinDiff(self, A,N,M):
        A.sort()
        l=0
        i=M-1
        diff=A[i]-A[l]
        ans=diff
        # print(A)
        # print(ans)
    
        while(i<N-1):
            l+=1
            i+=1
            diff=A[i]-A[l]
            ans=min(ans,diff)
        return ans
            
            
            
        

        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends