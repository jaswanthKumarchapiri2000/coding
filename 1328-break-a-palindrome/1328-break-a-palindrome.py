class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        k=len(palindrome)
        palindrome=list(palindrome)
        if k==1 :
            return ""
        for i in range(k):
            
            if palindrome[i]=='a' and i!=k-1:
                continue
            elif palindrome[i]=='a' and i==k-1:
                palindrome[i]='b'
            else:
                if k%2 ==1 and i==k//2:
                    continue
                palindrome[i]='a'
                break
        return ''.join(palindrome)        
        
        