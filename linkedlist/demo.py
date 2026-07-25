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


        




            


            



    
            


        