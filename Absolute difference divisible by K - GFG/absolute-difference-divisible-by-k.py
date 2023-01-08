#User function Template for python3

class Solution:
    def countPairs (self, n, arr, k):
        ans=0
        rem=[0]*k
        for i in range(n):
            rem[arr[i]%k]+=1
        for i in rem:
            if i>=2:
                ans+=((i*(i-1))//2)
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        arr=list(map(int,input().split()))
        k=int(input())
        
        ob = Solution()
        print(ob.countPairs(n,arr,k))
# } Driver Code Ends