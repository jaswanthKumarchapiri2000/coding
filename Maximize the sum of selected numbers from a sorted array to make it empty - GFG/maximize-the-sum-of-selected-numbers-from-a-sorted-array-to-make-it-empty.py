#User function Template for python3

class Solution:
    
    def maximizeSum (self,arr, n) :
        sum=0
        maxi=max(arr)
        
        dict1=dict.fromkeys(range(0,maxi+1),0)
        for i in range(n):
            dict1[arr[i]]+=1
        i=maxi
        while(i >0):
            if dict1[i] >0:
                sum=sum+i
                dict1[i-1]=dict1[i-1]-1
                dict1[i]-=1
            else:
                i=i-1
        return sum
        #Complete the function



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    arr.sort()
    ob=Solution()
    
    ans = ob.maximizeSum(arr, n)
    print(ans)

    





# } Driver Code Ends