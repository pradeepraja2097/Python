import numpy as np
array=np.array([1,2,3])
array_copy=array.copy() #copy function stores the value in array_copy


array[0]=23 # it replaces the value 23 in 0th index


array_view=array.view()#it shows the updated value we can view the array values

print(array_copy) #it prints the copy value in the array
print(array) #it prints the updated value
print(array_view) #it prints the view value
 