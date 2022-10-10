class MyCalendarTwo:

    def __init__(self):
        self.array=[]
        

    def book(self, start: int, end: int) -> bool:
        self.array.append((start,1))
        self.array.append((end,-1))
        self.array.sort()
        count=0
        for pair in self.array:
            count+=pair[1]
            if count > 2 :
                self.array.remove((start,1))
                self.array.remove((end,-1))
                return False
        return True
            
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)