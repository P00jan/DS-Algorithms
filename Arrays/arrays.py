#so in python we have to import array module to use arrays
import array #or you can import the whole module like:
from array import *
a = array('i',[1,2,3,4])
for elements in a:
    print(f"{elements} is in the array")
# output of the above will be:
    '''
1 is ina the array
2 is ina the array
3 is ina the array
4 is ina the array
    '''
#Let's create a python program to understand array methods
# create a array with integers
int_arr = array('i',[10,20,30,40,50,60])
print(f"Original array is {int_arr}")

# append 30 and 60 to the array
int_arr.append(30)
int_arr.append(60)
print(f"After update: {int_arr}")
#output: After update: array('i', [10, 20, 30, 40, 50, 60, 30, 60])
      
#insert 90 at position 1 of the array
int_arr.insert(1,90)
print(f"After update: {int_arr}")
#Output: After update: array('i', [10, 90, 20, 30, 40, 50, 60, 30, 60]) 
 
#Removing an element from array
int_arr.remove(20)
print(f"After update: {int_arr}")
#Output:After update: array('i', [10, 90, 30, 40, 50, 60, 30, 60])

