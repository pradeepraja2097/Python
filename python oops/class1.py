class Demo:   # created class name called demo

    print("hello World") # we can directly access any data in class itself

    d=50 # variable can be given outside the function  but it is accessed by "self key"
    e=10
    def example(self,a,b): # created one argument called example ,"self" is the important keyword 
        c=a+b+self.d-self.e# performing addition operations
        #print(c) #Pinting the operations that performed
        return c # we  can access outside of the function


obj=Demo()    #created object name("obj" we can give any thing) is equal to demo
ans=obj.example(10,35) # Outside funcrions called here
print(ans)



