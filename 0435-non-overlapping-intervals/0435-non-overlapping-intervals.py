class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans=0
        intervals.sort(key = lambda x :x[1])
        low,high=intervals[0][0],intervals[0][1]
        for start,end in intervals[1:]:
            if start>=high :
                high=end
            else:
                ans+=1
        return ans