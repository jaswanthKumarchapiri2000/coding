class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        defeat=defaultdict(int)
        win=defaultdict(int)
        for a,b in matches:
            win[a]+=1
            defeat[b]+=1
        ans=[[],[]]
        for ele in win:
            if ele not in defeat:
                ans[0].append(ele)
        for ele2 in defeat:
            if defeat[ele2]==1:
                ans[1].append(ele2)
        # print(win,defeat)
        for ele in ans:
            ele.sort()
        return ans
        