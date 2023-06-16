import math
class Solution:
    def minimumSum(self, s : str) -> int:
        # code here
        i,j = 0,len(s)-1
        count = 0
        while(i<j):
            if s[i]!='?':count +=1
            if s[j]!='?':count +=1
            if s[i]!=s[j] and (s[j]!='?' and s[i]!='?'):
                return -1
            else:
                if s[i]!='?' and s[j]=='?':
                    s = s[:j]+s[i]+s[j+1:]
                elif s[i]=='?' and s[j]!='?':
                    s = s[:i]+s[j]+s[i+1:]
            i +=1
            j -=1
        l,ch,sum = len(s),'',0
        if count ==0 or count ==1:
            return 0

        for i in range(l):
            if s[i]!='?':
                ch = s[i]
                break
            
        for i in range(l):
            if s[i]!='?':
                ch = s[i]
            if s[i]=='?':
                s = s[:i]+ch+s[i+1:]
               
        for i in range(l-1):
            sum += abs(ord(s[i])-ord(s[i+1]))
        return sum   



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        s = (input())
        
        obj = Solution()
        res = obj.minimumSum(s)
        
        print(res)
        

# } Driver Code Ends