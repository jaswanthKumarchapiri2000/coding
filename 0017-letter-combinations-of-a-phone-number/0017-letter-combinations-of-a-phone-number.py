class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n=len(digits)
        ans=[]
        res=[]
        for i in range(len(digits)):
            ele=digits[i]
            if ele <= "6":
                ele=int(ele)
                intial=97+(ele-2)*3
                ans.append([chr(intial),chr(intial+1),chr(intial+2)])
            else:
                if ele=="7":
                    ans.append(["p","q","r","s"])
                if ele=="8":
                    ans.append(["t","u","v"])
                if ele=="9":
                    ans.append(["w","x","y","z"])
        for i in range(n):
            if i==0:
                res=ans[0]
            else:
                new=[]
                present=ans[i]
                for ch in present:
                    for each in res:
                        new.append(each+ch)
                res=new


        return res