class MyCalendarThree:

    def __init__(self):
        self.array=[]
        
        

    def book(self, start: int, end: int) -> int:
        i=bisect.bisect_left(self.array,(start,1))
        self.array.insert(i,(start,1))
        j=bisect.bisect_left(self.array,(start,1))
        self.array.insert(j,(end,-1))
        self.array.sort()
        maxi=0
        count=0
        for pair in self.array:
            count+=pair[1]
            maxi=max(maxi,count)
        return maxi
        
        
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)