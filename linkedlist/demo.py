# # class Node:
# #     def __init__(self,data=None,next=None):
# #         self.data=data
# #         self.next=next
# # class linkedlist:
# #     def __init__(self):
# #         self.head=None
# #     def print(self):
# #         if self.head is None:
# #             return "Linked list is empty"
# #         itr=self.head
# #         lstr=""
# #         while itr:


# class Node:
#     def __init__(self,data=None):
#         self.data=data
#         self.ref=None

# class LinkedList:
#     def __init__(self):
#         self.head=None

#     def print_ll(self):
#         if self.head is None:
#             print("linked list is empty")
#             return 
#         node=self.head
#         while node:
#             print(node.data,end="->")
#             node=node.ref
#         print("None")

#     def add_beg(self,data):
#         new_node=Node(data)
#         new_node.ref=self.head
#         self.head=new_node

#     def add_end(self,data):
#         # new_node=Node(data)
#         if self.head is None:
#             # self.head=new_node
#             self.add_beg(data)
#             return
#         node=self.head
#         while node:
#             node=node.ref
#         self.add_beg(data)


class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class Linked_List:
    def __init__(self):
        self.head=None

    def print_ll(self):
        if self.head is None:
            print("Linked list is empty")
            return 
        else:
            node=self.head
            while node is not None:
                print(node.data,end="->")
                node=node.ref
            print("None")

    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            node=self.head
            while node.ref is not None:
                node=node.ref
            node.ref=new_node
    def add_position(self,data,ele):
        node=self.head
        while node is not None:
            if node.data==ele:
                new_node=Node(data)
                new_node.ref=node.ref
                node.ref=new_node

                # prevref=node.ref
                # node.ref=new_node
                # node.ref=prevref
                return
            else:
                node=node.ref
        else:
            print("Element not found")

    def delete_begin(self):
        if self.head is None:
            print("LL is already empty")
        # data=self.head
        else:
            self.head=self.head.ref
            print("Node deleted successfully")
    def delete_end(self):
        if self.head is None:
            print("LL is already empty")
            return 
        elif self.head.ref is None:
            self.head=None
            return 
        else:
            node=self.head
            while node.ref.ref is not None:
                node=node.ref
            node.ref=None
            return 

    def delete_ele(self,ele):
        node=self.head
        if node is None:
            print("LL is empty")
            return
        if node.data==ele:
            self.head=node.ref
        else:
            while  node.ref is not None and node.ref.data!=ele :
                node=node.ref
            if node.ref is None:
                print("element Not Found")
                return 
            else:
                node.ref=node.ref.ref
                return 

    def update_ele(self,ele,up):
        node=self.head
        while node is not None:
            if node.data==ele:
                node.data=up
                return 
            node=node.ref
        else:
            print("element not found")
        
        # while node.data!=ele:
        #     node=node.ref
        # if node.data==ele:
        #     node.data=up
        # else:
        #     print("Element not found")
        #     return 

ll = Linked_List()

ll.add_end(10)
ll.add_end(20)
ll.add_end(30)
ll.print_ll()  

ll.add_begin(5)
ll.print_ll()

ll.add_position(25, 20)
ll.print_ll()
        
ll.delete_ele(20)
ll.print_ll()



        
        
        




            


            



    
            


        