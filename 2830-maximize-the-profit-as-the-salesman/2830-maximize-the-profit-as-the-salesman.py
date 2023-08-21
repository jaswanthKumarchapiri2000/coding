class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        offers.sort(key=lambda a: a[1])
        ends = [o[1] for o in offers]
        m = len(offers)
        dp = [0]*m
        for i in range(m):
            s, e, g = offers[i]
            j = bisect_right(ends, s-1)
            bestPrevDp = dp[j-1] if i > 0 else 0
            dp[i] = max(dp[i-1] if i > 0 else 0, bestPrevDp + g)
        return dp[-1]