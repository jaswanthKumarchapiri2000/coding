#User function Template for python3

class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        #Code here
        a.append(k)
        n=n+1
        l=0
        i=0
        ans,prod=0,1
        while(l <n and  i<n ):
            ele=a[i]
            prod*=ele
            while (prod >= k and l<=i):
                ans+=(i-l)
                prod=prod//a[l]
                l+=1
            i+=1
        
        
        
        # print(l,i)
                
        return ans
            
            
    
    
    
    


#{ 
 # Driver Code Starts

#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        
        print(Solution().countSubArrayProductLessThanK(arr, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends