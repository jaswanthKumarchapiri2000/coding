#User function Template for python3

class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        # code here
        if low >= high :
            return
        mid= (low+high)//2
        arr[mid],arr[high]=arr[high],arr[mid]
        # print(arr,low,high)
        ind=self.partition(arr,low,high)
        # print(ind,arr,"\n")
        self.quickSort(arr,low,ind-1)
        self.quickSort(arr,ind+1,high)
        
        
            
    
    def partition(self,arr,low,high):
        # code here
        # print(arr,low,high)
        pivot=arr[high]
        left=low-1
        for i in range(low,high):
            if arr[i] <= pivot:
                left=left+1
                arr[left],arr[i]=arr[i],arr[left]
        arr[left+1],arr[high]=arr[high],arr[left+1]
        return left+1
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends