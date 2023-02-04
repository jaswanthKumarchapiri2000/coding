#User function Template for python3

class Solution:

    #Function to perform case-specific sorting of strings.
    def caseSort(self,s,n):
        #code here
        ans=''
        lc=[]
        uc=[]
        for ele in s:
            if ord(ele) >= 96:
                lc.append(ele)
            else:
                uc.append(ele)
        lc.sort()
        uc.sort()
        i,j=0,0
        
        for b in range(n) :
            ele=s[b]
            if ord(ele) >= 96:
                ans+=lc[i]
                i+=1
            else:
                ans+=uc[j]
                j+=1
        return ans
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        s=str(input())
        print(Solution().caseSort(s,n))
# } Driver Code Ends