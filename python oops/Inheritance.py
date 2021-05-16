
# Single Inheritance

class father():
    f_name="Raja"
    f_age= 56

class son(father):     
    s_name="Pradeep"
    S_age="24"
    
obj=son()
print("father name is",obj.f_name)
print("Son name is",obj.s_name)

# Multilevel Inheritance

class grandfather():
    g_name="Rama"
    g_age= 56

class father1(grandfather):
    f_name="lakshman"
    f_age= 45

class son1(father1):
    s_name="Pradeep"
    S_age="24"
    
obj=son1()
print("father name is",obj.f_name)
print("Son name is",obj.s_name)
print("grand father name is",obj.g_name)