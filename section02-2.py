# Section02-2
# Python Basic Coding
# Warm up coding practice

# import this
import sys

# python basic encoding
print(sys.stdin.encoding)
print(sys.stdout.encoding)

# print statement
print('My name is Goodboy!')

# variable declaration
myName = 'Goodboy'

# condition statement
if myName == 'Goodboy':
    print('Hello Goodboy!') 
    
# loop statement
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = %d' % (i, j, i*j))

# variable assignment in Korean
이름 = "좋은사람"
print(이름)

# function declaration
def greeting():
    print('Hello Goodboy!')

# class declaration
class Cookie:
    pass

# class instance
cookie = Cookie()
print(id(cookie))
print(dir(cookie))

        