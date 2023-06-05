#User function Template for python3

class Solution:
    def reverseEqn(self, s):
        # code here
        ans=""
        num=""
        helper=['+','-','/','*']
        for ele in s[::-1]:
            if ele in helper:
                ans+=num
                ans+=ele
                num=""
                continue
            num=ele+num
        return ans+num
            
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.reverseEqn(s)
        print(ans)
# } Driver Code Ends