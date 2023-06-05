#User function Template for python3

from typing import List
from collections import deque

class Solution:    
    def eventualSafeNodes(self, V : int, adj : List[List[int]]) -> List[int]:
        # code here
        
        ans=[]
        q=deque()
        visited=[0]*V
        indegree=[0]*V
        rev=[[] for i in range(V)]
        # print(V,adj)
        for i in range(V):
            for ele in adj[i]:
                rev[ele].append(i)
                indegree[i]+=1
        # print(rev)
        

        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        # print(visited)
        while(q):
            ele=q.pop()
            ans.append(ele)
            for side in rev[ele]:
                indegree[side]-=1
                if indegree[side]==0:
                    q.append(side)
        
        
        
                
        
        ans.sort()    
        return ans
                
                



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v = map(int, input().strip().split())
            adj[u].append(v)
        obj = Solution()
        ans = obj.eventualSafeNodes(V, adj)
        for nodes in ans:
            print(nodes, end = ' ')
        print()
            


# } Driver Code Ends