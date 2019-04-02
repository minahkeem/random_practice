#2.1 Remove Duplicates
 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_dups(head):
    n = head
    while(n is not None):
        checker = n.next
        prev = n
        while(checker is not None):
            if(n.data == checker.data):
                prev.next = checker.next
                checker = prev.next
            else:
                prev = prev.next
                checker = checker.next
        n = n.next
        
        
#TESTING

def main():
    #2.1
    head = Node("a")
    head.next = Node("b")
    head.next.next = Node("c")
    head.next.next.next = Node("b")
    head.next.next.next.next = Node("b")
    head.next.next.next.next.next = Node("d")
    head.next.next.next.next.next.next = Node("a")
    head.next.next.next.next.next.next.next = Node("e")
    
    temp = head
    while(temp != None):
        print(temp.data)
        temp = temp.next
    print("---------")
    remove_dups(head)
    temp = head
    while(temp != None):
        print(temp.data)
        temp = temp.next
        
main()