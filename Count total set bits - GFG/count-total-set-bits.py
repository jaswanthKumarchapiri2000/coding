#User function Template for python3

class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBits(self,N):
        # code here
        # return the count
        count = 0
        for i in range(31):
            x = 1 << i # calculate the ith bit
            y = (N + 1) // (x * 2) * x # count the number of set bits up to the ith bit
            z = (N + 1) % (x * 2) - x # count the number of set bits in the ith bit
            count += y + max(z, 0) # add the counts to the total
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        ob=Solution()
        print(ob.countSetBits(int(input())))
# } Driver Code Ends