#User function Template for python3

class Solution():
    def solve(self, val, arr, k):
        n = len(arr)
        sumo = 0
        for i in range(n):
            if sumo >=val:
                sumo = 0
                k -= 1
            sumo += arr[i]
        if sumo >=val:
            k-=1
        if k > -1:
            return False
        return True
            
    def maxSweetness(self, sweetness, n, k):
        l = 0
        r = sum(sweetness)
        # print("here", self.solve(9, sweetness, k))
        while l <= r:
            mid = (l+r) //2
            if self.solve(mid, sweetness, k):
                ans = mid
                l=mid+1
            else:
                r = mid -1
        return ans
        while r:
            if self.solve(r, sweetness, k):
                return r
            r -= 1
#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(int(input())):
    n,k = map(int, input().split())
    sweetness = [int(i) for i in input().split()]
    print(Solution().maxSweetness(sweetness, n,k))
# } Driver Code Ends