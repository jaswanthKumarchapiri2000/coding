class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ans=0
        d={}
            
        for i in range(len(words)):
            if d.get(words[i][::-1],0)!=0:
                d[words[i][::-1]]+=1
                if d[words[i][::-1]]>=2:
                    ans+=4
                    d[words[i][::-1]]-=2
            elif d.get(words[i],0)!=0:
                d[words[i]]+=1
            else:
                d[words[i]]=1
                
                
                
                    
        for i in range(len(words)):
            if words[i] == words[i][::-1] and d[words[i]]==1:
                ans+=2
                break
        return ans
                    
        