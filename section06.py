# Section06
# Python Function and Lambda

# Function Definition
# def function_name(parameter):
#     code
#     function call
# function_name(parameter)

# example 1
def hello(world):
    print('Hello', world)

hello("Python!")
hello(7777)

# example 2
def hello_return(world):
    val = "Hello" + str(world)
    return val

str = hello_return("Python!!!!")
print(str)

# example 3(multiple return)
def hello_return_multiple(x):
    y1 = x * 100
    y2 = x * 1000
    y3 = x * 10000
    return y1, y2, y3

val1, val2, val3 = hello_return_multiple(1)
print(val1, val2, val3)

# example 4(multiple return) list
def hello_return_multiple(x):
    y1 = x * 100
    y2 = x * 1000
    y3 = x * 10000
    return [y1, y2, y3]

lt = hello_return_multiple(100)
print(lt)

# example 5
# *args, *kwargs
def args_func(*args):
    print(args)

args_func('kim')
args_func('kim', 'park')
args_func('kim', 'park', 'lee')

# kwargs
def kwargs_func(**kwargs):
    print(kwargs)

kwargs_func(name='kim', name2='park', name3='lee')

def test(x, y, z=0):
    print(x, y, z)


    
    