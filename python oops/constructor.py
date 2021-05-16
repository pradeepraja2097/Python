class Demo:
    def __init__(self,name,age):  # constructor was initialized in class itself
        self.name=name # self is a key word to call functions
        self.age=age
    def display(self): # display is a function It can be declare both inside tha class and outside the class
        print("the name is",self.name)
        print("the age is",self.age)

obj1=Demo("vijay",30)
obj2=Demo("Pradeep",25)
obj1.display()
obj2.display()

