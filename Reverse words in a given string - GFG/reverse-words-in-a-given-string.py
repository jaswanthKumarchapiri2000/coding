# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here 
        S=list(map(str,S.split(".")))
        S=S[::-1]
        ans=''
        for ele in S:
            ans+=ele
            ans+='.'
        ans=ans[:-1]
        return ans


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends