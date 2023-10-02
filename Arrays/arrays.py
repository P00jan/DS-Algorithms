#so in python we have to import array module to use arrays
import array #or you can import the whole module like:
from array import *
a = array('i',[1,2,3,4])
for elements in a:
    print(f"{elements} is ina the array")

#Let's create a python program to understand array methods
# create a array with integers
int_arr = array('i',[10,20,30,40,50,60])
print(f"Original array is {int_arr}")