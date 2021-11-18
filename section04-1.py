# section04-1
# data type

v_str1 = "Niceman"
v_bool = True
v_str2 = "Goodboy"
v_float = 10.3
v_int = 7
v_dict = {
    "name": "John",
    "age": 30    
}
v_tuple = 3, 5, 7
v_list = [4, 5, 6]
v_set = {1, 2, 3}

print(type(v_str1))
print(type(v_bool))
print(type(v_str2))
print(type(v_float))
print(type(v_int))
print(type(v_dict))
print(type(v_tuple))
print(type(v_list))
print(type(v_set))

i1 = 39
i2 = 939
big_int1 = 9999999999999999999999999999999
big_int2 = 7777777777777777777777777777777
f1 = 1.234
f2 = 3.14
f3 = .5
f4 = 10.

print(i1 * i2)
print(big_int1 * big_int2)
print(f1 ** f2)
print(f3 + i2)

result = f3 + i2
print(result, type(result))

a = 5.
b = 4
c = 10

print(type(a), type(b))
result2 = a + b
print(result2)

# type change
# int, float, complex

print(int(result2))
print(float(c))
print(complex(3))
print(int(True))
print(int(False))
print(int('3'))
print(complex(False))

y = 100
y += 100
print(y)

# math function
# https://docs.python.org/3/library/math.html
print(abs(-7))
n, m = divmod(100, 8)
print(n, m)

import math

print(math.ceil(5.1))
print(math.floor(5.9))

