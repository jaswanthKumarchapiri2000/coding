#User function Template for python3

class Solution:
    def kthElement(self,  nums1, nums2, m, n, k):
        if m > n:
            return self.kthElement(nums2, nums1, n, m, k)
        low = max(0,k-n-1)
        high = min(k,m)
        # print(low,high)
        while low <= high:
            cut1 = (low+high)//2
            cut2 = k - cut1
            # print(cut1,cut2,m,n)
            l1 = float('-inf') if cut1 == 0 else nums1[cut1-1]
            l2 = float('-inf') if cut2 == 0 else nums2[cut2-1]
            r1 = float('inf') if cut1 == m else nums1[cut1]
            r2 = float('inf') if cut2 == n else nums2[cut2]
            if l1 <= r2 and l2 <= r1:
                return max(l1, l2)
            elif l1 > r2:
                high = cut1-1
            else:
                low = cut1+1
        return 1

        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m, k = sz[0], sz[1], sz[2]
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement( a, b, n, m, k))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends