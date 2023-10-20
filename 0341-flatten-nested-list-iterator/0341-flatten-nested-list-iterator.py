# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    
    def __init__(self, nestedList: [NestedInteger]):
        self.ind=0
        self.ans=[]
        for ele in nestedList:
            if ele.isInteger():
                temp=ele.getInteger()
                self.ans.append(temp)
                
            else:
                helper=ele.getList()
                def acs(a,b):
                    for ele in a:
                        if ele.isInteger():
                            temp=ele.getInteger()
                            b.append(temp)
                        else:
                            temp=ele.getList()
                            acs(temp,b)
                acs(helper,self.ans)
                            
        self.n=len(self.ans)
                    
            
            
        
    
    def next(self) -> int:
        temp=self.ans[self.ind]
        self.ind+=1
        return temp
        
        
    
    def hasNext(self) -> bool:
        if self.ind<self.n:
            return True
        return False
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())