#User function Template for python3
class Solution:
    def findKRotation(self,arr,  n):
        # code here
        low=0
        high=n-1
        while (low <= high):
            mid=(low+high)//2
            if mid==low and mid==high:
                return mid
            if mid==0:
                if arr[mid] <arr[mid+1]:
                    return 0
            if mid==n-1:
                if arr[mid] < arr[mid-1]:
                    return mid
            if mid < n-1 and mid > 0 :
                if (arr[mid] < arr[mid+1]) and (arr[mid] < arr[mid-1] ):
                    return mid
            if arr[mid] > arr[high]:
                low=mid+1
            else:
                high=mid-1
            
                



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	tc=int(input())
	while tc > 0:
		n=int(input())
		a=list(map(int , input().strip().split()))
		ob = Solution()
		ans=ob.findKRotation(a, n)
		print(ans)
		tc=tc-1



# } Driver Code Ends