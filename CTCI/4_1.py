# 4.1 Route Between Nodes

class Node():
    def __init__(self, data = None, children = None):
        self.data = data
        self.children = children
        
    def add_child(self, data):
        self.children.append(node)
        
def route_between_nodes(start, end):
    queue = []
    checker = {}
    curr = start
    queue.append(curr)
    while(len(queue) > 0):
        if(curr.data == end.data):
            return True
        queue.pop(0)
        checker[curr.data] = None
        if(curr.children is not None):
            for child in curr.children:
                if(child.data not in checker):
                    queue.append(child)
        if(len(queue) > 0):
            curr = queue[0]
    return False

def main():
    start = Node(1, [Node(2), Node(3), Node(4)])
    start.children[0].children = [start, Node(5), Node(6)]
    start.children[2].children = [Node(7), Node(8)]
    start.children[2].children[1].children = [Node(9), start.children[0].children[2]]
    
    end1 = Node(4)
    end2 = Node(8)
    end3 = Node(10)
    
    print(route_between_nodes(start, end1))
    print(route_between_nodes(start, end2))
    print(route_between_nodes(start, end3))

main()