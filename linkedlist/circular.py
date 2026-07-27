class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class CircularLL:
    def __init__(self):
        self.head=None

    def printcll(self):
        node=self.head
        if node is None:
            print("LL is empty")
            return
        while node is not None:
            print(node.data,end="->")
            node=node.ref

            if node ==self.head:
                break
        print("head")

    def add_begin(self,data):
        new_node=Node(data)

        node=self.head
        if node is None:
            self.head=new_node
            new_node.ref=self.head
            return 
        while node.ref is not self.head:
            node=node.ref
        new_node.ref=self.head
        node.ref=new_node
        self.head=new_node
        
        

        