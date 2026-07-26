class Node:
    def __init__(self,data):
        self.prevp=None
        self.data=data
        self.nextp=None
class DoublyLL:
    def __init__(self):
        self.head=None

    def print_fll(self):
        if self.head is None:
            print("LL is empty")
            return 
        node=self.head
        while node is not None:
            print(node.data,end="->")
            node=node.nextp
    def print_rll(self):
        if self.head is None:
            print("LL is Empty")
            return 
        node=self.head
        while node.nextp is not None:
                node=node.nextp
        while node is not None:
            print(node.data,end="->")
            node=node.prevp

    def add_begin(self,data):
        node=self.head
        new_node=Node(data)
        if node is None:
            self.head=new_node
            return 
        else:
            x=self.head
            new_node.nextp=x
            self.head.prevp=new_node
            self.head=new_node

        
    def add_end(self,data):
        new_node=Node(data)
        node=self.head
        if self.head is None:
            self.head=new_node
            return 
        else:
            while node.nextp is not None:
                node=node.nextp
            new_node.prevp=node
            node.nextp=new_node

    def add_position(self,data,ele):
        new_node=Node(data)
        node=self.head
        if node is None:
            print("list is empty")
            return 
        while node is not None:
            if node.data==ele:
                previous_node = node.prevp
                new_node.prevp = previous_node
                new_node.nextp = node
                if previous_node is None:
                    self.head = new_node
                else:
                    previous_node.nextp = new_node
                node.prevp = new_node
                return
            node=node.nextp
        print("element Not Found")





        
        