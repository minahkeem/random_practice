#3.2 Stack Min
class Min_Stack:
    class Node:
        def __init__(self, data=None):
            self.next = None
            self.data = data
            self.prev_min = None
    
    def __init__(self):
        self.top = None
        self.min = None
        
    def show_top(self):
        return self.top.data
        
    def push(self, item):
        if(self.top == None):
            self.top = Min_Stack.Node(item)
            self.min = self.top
            self.prev_min = self.top
        else:
            temp = Min_Stack.Node(item)
            if(temp.data < self.min.data):
                prev_min = self.min
                self.min = temp
                self.min.prev_min = prev_min
            temp.next = self.top
            self.top = temp
            
    def pop(self):
        if(self.top == None):
            print("Error: Empty Stack")
            return
        if(self.top == self.min):
            self.min = self.min.prev_min
        temp = self.top.data
        self.top = self.top.next
        return temp
    
    def min_val(self):
        return self.min.data
    
def main():
    s = Min_Stack()
    s.push(4)
    s.push(5)
    s.push(3)
    s.push(1)
    print(s.min_val()) #1
    s.push(2)
    print(s.show_top()) #2
    print(s.min_val()) #1
    s.pop()
    print(s.min_val()) #1
    s.pop()
    print(s.min_val()) #3
    s.pop()
    print(s.min_val()) #4
    
main()