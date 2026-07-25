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


        
        
        




            


            



    
            


        