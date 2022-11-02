class Solution:
    def viablemutation(self,start,nextmutation):
        count=0
        for i in range(len(start)):
            if start[i]!=nextmutation[i]:
                count+=1
        return count==1
                
        
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        a=collections.deque()
        a.append([start,start,0])
        while(a):
            current,prev,nsteps=a.popleft()
            if current==end:
                return nsteps
            for string in bank:
                if self.viablemutation(current,string) and string!=prev:
                    a.append([string,current,nsteps+1])
        return -1
        
                        
        