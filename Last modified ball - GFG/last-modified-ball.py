#User function Template for python3

class Solution():
    def solve(self, N, A):
        #your code here
        if A[N-1]<9:
            return N
        else:
            N=N-1
            while(N>0):
                if A[N] < 9:
                    return N+1
                else:
                    N=N-1
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(int(input())):
    n = int(input())
    array=[int(i) for i in input().split()]
    obj = Solution()
    print(obj.solve(n, array))
# } Driver Code Ends