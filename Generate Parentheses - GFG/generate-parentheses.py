#User function Template for python3

class Solution:
    def AllParenthesis(self,n):
        #code here
        ans=[]
        def helper(left,right,string):
            nonlocal ans,n
            if left==n and right==n:
                ans.append(string)
            else:
                if right > left:
                    return 
                else:
                    if right==left:
                        helper(left+1,right,string+'(')
                    else:
                        if left==n:
                            helper(left,right+1,string+')')
                        else:
                            helper(left,right+1,string+')')
                            helper(left+1,right,string+'(')
        helper(0,0,'')
        return ans
                            
                        
                        
            
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3


        
if __name__=="__main__":
    t=int(input())
    for i in range(0,t):
        n=int(input())
        ob=Solution()
        result=ob.AllParenthesis(n)
        result.sort()
        for i in range(0,len(result)):
            print(result[i])
        

# } Driver Code Ends