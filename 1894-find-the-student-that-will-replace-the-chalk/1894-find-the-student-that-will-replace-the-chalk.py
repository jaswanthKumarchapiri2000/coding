class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n=len(chalk)
        i=0
        s=sum(chalk)
        while( k > s):
            k=k%s
        while(chalk[i] <=k):
            k=k-chalk[i%n]
            i=(i+1)%n
        return i%n
        