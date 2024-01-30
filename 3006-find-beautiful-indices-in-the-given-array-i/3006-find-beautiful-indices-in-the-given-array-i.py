class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        n=len(a)
        m=len(b)
        ans=[]
        slen=len(s)
        irange=slen-n
        jrange=slen-m
        temp1,temp2=[],[]
        for i in range(irange+1):
            if s[i:i+n]==a:
                temp1.append(i)
        for j in range(jrange+1):
            if s[j:j+m]==b:
                temp2.append(j)
        for ele in temp1:
            for ele2 in temp2:
                if abs(ele-ele2) <= k:
                    ans.append(ele)
                    break
        ans.sort()
        return ans
        