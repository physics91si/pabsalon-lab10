class Set:
    def __init__(self):
        self.list = []
    def __contains__(self, element):
        for elem in self.list:
            if elem == element:
                return True
            return False
    
    def __add__(self, element):
        self.list.append(element)
        
    def __remove__(self,element):
        if self.list.__contains__(element):
            self.list.remove(element)
        
    def __size__(self):
        count = 0
        for i in self.list:
            count = count + 1
        return count
    def __str__(self):
        return str(self.list)
    
    def __or__(self,other):
        newList = []
        for i in self.list + other:
            newList.append(i)
        return newList
            
        