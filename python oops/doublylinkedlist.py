class Node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None
class doublyLL:
    def __init__(self):
        self.head=None
    def print_dll(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
    
    def print_dll_reverse (self):
        if self.head is None:
            print("linked list is empty")
        else:
             n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data)