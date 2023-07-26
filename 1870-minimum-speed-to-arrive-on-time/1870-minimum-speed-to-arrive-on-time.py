class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def ispossible(speed):
            n=len(dist)
            ans=0
            for i in range(n):
                ele=dist[i]
                if ele%speed==0:
                    ans+=ele//speed
                else:
                    if i!=n-1 :
                        ans+=ele//speed+1
                    else:
                        ans+=ele/speed
            return ans <= hour
        low=max(1,sum(dist)//hour)
        low=int(low)
        high=int(1e9)
        ret=-1
        while(low <= high):
            # print(low,high)
            mid=(low+high)//2
            if ispossible(mid):
                # print("for mid",mid)
                ret=mid
                high=mid-1
            else:
                low=mid+1
        return ret
       
                    
            
        