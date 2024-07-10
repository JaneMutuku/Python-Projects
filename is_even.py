#function examples
from math import sqrt

#Built in function
x = sqrt(100)
print ('Square root is: ', x)

#user functions
def even(number):
    #This function checks if a number is even
    if number %2 == 0:
        print(number, 'is even')
    else:
        print(number, 'is not even')
        even()
