#addition implementation
def add(x,y):
    return x+y 
    
#subtraction implementation
def subtract(x,y):
    return x-y                   #on master branch

#multiply implimentaon
def multiply(x,y):
    return x*y              #implemented on bug456

#divide implementaion
def divide(x,y):
    if y==0:               #Implemented on master Branch 
        return DIVIDE_BY_0_ERROR
    else:
        return x/y
def square(x):
    return x*x 