#User function Template for python3
from collections import defaultdict,deque
class Solution:
    def findOrder(self,a, N, K):
        d=defaultdict(list)
        q=deque()
        ans=""
        indegree=defaultdict(int)
        count=0
        for ele in a:
            for ch in ele:
                if ch not in d:
                    d[ch]=[]
                    count+=1
            if count==k:
                break
                    
        for i in range(N-1):
            # print(d)
            first=a[i]
            len1=len(first)
            second=a[i+1]
            len2=len(second)
            ind1,ind2=0,0
            flag=0
            while(flag==0 and ind1<len1 and ind2< len2):
                if first[ind1] != second[ind2] :
                    d[first[ind1]].append(second[ind2])
                    indegree[second[ind2]]+=1
                    flag=1
                ind1+=1
                ind2+=1
        for ele in d.keys():
            if indegree[ele]==0:
                q.append(ele)
        while(q):
            ele=q.pop()
            ans+=ele
            for adj in d[ele]:
                indegree[adj]-=1
                if indegree[adj]==0:
                    q.append(adj)
        # print(ans)
        return ans
                
                
    # code here
    
    
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends