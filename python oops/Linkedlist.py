
#reffered in amulyas academy youtube vedio 
class Node: 
    def __init__(self,data):# Creating Node ,(Node contains data and reference)
        self.data=data
        self.ref=None               
class linkedlist:
    def __init__(self):#It is used to connect the linked list with head,head means (data,ref)
        self.head=None
    
    def print_linkedlist(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n is None:
                print(n.data)# for accessing data alone,because it contains both data and ref node
                n=n.ref# to access the next node ,so we are giving n=n.ref
    
    def add_begin(self,data): #adding new node at the beggining
        new_node=Node(data) # from the class creating new node ,accessed by the class function
        new_node.ref=self.head# new node is created so head to be changed from old node to new node
        self.head=new_node
    
    def add_end(self,data):# adding new node to the end
        new_node=Node(data)# from the class creating new node ,accessed by the class function
        if self.head is None:# check whether linked list is empty are not
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
                n.ref=new_node
    
    def add_after(self,data,x):
        n=self.head()
        while n is not None:
            if x == n.data:
                break
            n= n.ref
        if  n is None:
            print("Node is not present in LL")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
    def insert_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node

    def delete_begin(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            self.head()= self.head.ref

    def delete_by_value(self,x):
        if self.head is None:
            print("LL is empty")
        if x==self.head.data:
            self.head=self.head.ref
            return
        n=self.head
        while n.ref is not None:
            if x==n.ref.data:
                break
            n=n.ref
        if n.ref is None:
            print("Node is not present")
        else:
            n.ref=n.ref.ref



Linked_list=linkedlist()
Linked_list.add_begin(10)
Linked_list.add_end(10)
Linked_list.add_begin(20)
Linked_list.print_linkedlist()


    