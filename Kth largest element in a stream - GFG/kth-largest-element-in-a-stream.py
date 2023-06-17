#User function Template for python3
import heapq
class Solution:
    def kthLargest(self, k, arr, n):
        # code here
        minheap=[]
        size=0
        ans=[]
        for ele in arr:
            if size < k-1:
                ans.append(-1)
                heapq.heappush(minheap,ele)
            elif size==k-1:
                heapq.heappush(minheap,ele)
                ans.append(minheap[0])
            else:
                if minheap[0] < ele:
                    heapq.heappop(minheap)
                    heapq.heappush(minheap,ele)
                    ans.append(minheap[0])
                else:
                    ans.append(minheap[0])
            size+=1
        return ans
                
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        k,n=map(int,input().split())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(*ob.kthLargest(k,arr,n))
# } Driver Code Ends