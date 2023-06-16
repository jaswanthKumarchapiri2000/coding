class Solution:
    def stringMirror(self, str : str) -> str:
        # code here
        ans=""
        for ele in str:
            if ans:
                if ans[-1] < ele :
                    return ans+ans[::-1]
                elif ans[-1] ==ele :
                    temp=ans+ele
                    if temp + temp[::-1] <= ans+ans[::-1]:
                        ans+=ele
                    else:
                        return ans+ans[::-1]
                else:
                    ans+=ele
                
            else:
                ans+=ele
        return ans+ans[::-1]
        



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        str = (input())
        
        obj = Solution()
        res = obj.stringMirror(str)
        
        print(res)
        

# } Driver Code Ends