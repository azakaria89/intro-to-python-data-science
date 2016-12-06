__author__ = "Ahmed Zakaria"
import math as m
##Instructions for the following simple exercise
# Use print() in combination with type() to print out the type of var1.
# Use len() to get the length of the list var1. Wrap it in a print() call to directly print it out.
# Use int() to convert var2 to an integer. Store the output as out2.

# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True
# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))  #len also works on strings to find the number of chars

# Convert var2 to an integer: out2
out2=int(var2)
#help function is used to get info about any function
help(round) #or from the ipython use ?round
################################################################################################
#Optional arguments way of definition
#def function (real[img]) #img is optional or another way def function (real,img=0) img is optional with default value =0
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# concatente together first and second: full
full=first+second
# Sort full in descending order: full_sorted
full_sorted=sorted(full,reverse=True)  #reverse =True in order to make the sorting descending
# Print out full_sorted
print(full_sorted)
##########################objects methods#######################################################
# Everything in py is object and Each Object has a type e.g a list, a string,etc and each object has a set of methods varies according to its type
#String and list Methods
name=" ahmed zakaria"
name_upper=name.upper() #AHMED ZAKARIA you can always use help(str.upper)
num_of_As=name.count("a")
heights=[160,178.5,140,168,160]
print (heights.index(160)) #L.index(value, [start, [stop]]) -> integer -- return first index of value.
print (heights.count(160))
heights.reverse() #reverse the order of the elements in the list
heights.append(180) #as append takes on argument only
heights.append(200)
print(heights)
################################impoting packages example ################################################
from math import radians #explicit way of importing specific function in the package, import math.radians is not correct as radians is a function and not a subpackage
# Definition of radius
r = 192500
# Travel distance of Moon if 12 degrees. Store in dist.
dist=r*radians(12)

# Print out dist
print(dist)
#from scipy.linalg import inv as my_inv : this imports the inv function and give it an easy name using the as keyworkd from the subpackage linalg inside the scipy