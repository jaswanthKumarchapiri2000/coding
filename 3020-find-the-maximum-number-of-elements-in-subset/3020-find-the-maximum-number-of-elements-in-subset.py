class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n=len(nums)
        ans=1
        d=defaultdict(int)
        nums.sort()
        d2=defaultdict(lambda : 1)
        
        for i,ele in enumerate(nums):
            if sqrt(ele) in d:
                if d[sqrt(ele)]>=2 :
                    d2[ele]=2+d2[sqrt(ele)]
           
                    
            d[ele]+=1 
        d2[1]= d[1] if d[1]%2==1 else d[1]-1
        if d2[1] <= 1 :
            d2[1]=1
        return max(d2.values()) if len(d2) > 0 else 1
                
        