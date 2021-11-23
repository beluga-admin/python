# Section04-3
# pyton data type(자료형)
# List and Tuples

a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana', 'Orange']
e = [10, 100, ['Pen', 'Banana', 'Orange']]

# Indexing
print(d[3])
print(d[-2])
print(d[0]+d[1])
print(e[2][1])

# slice
print(d[0:1])
print(e[2][1:3])
print(c + d)
print(c * 3)
print(str(c[0])+'hi')
c[0] = 77
print(c)

del c[1]
print(c)
del c[-1]
print(c)

# List functions
y = [5, 2, 3, 1, 4]
print(y)
y.append(6)
print(y)
y.sort()
print(y)
y.reverse()
print(y)
y.insert(2, 7)
print(y)
y.remove(2)
y.remove(7)
print(y)
y.pop()
print(y)
ex = [88, 77]
y.extend(ex)
print(y)

# Tuple (orderable, repeatable, uneditable, unable to dele
a = ()
b = (1, )
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

print(c[2])
print(c[3])
print(d[2][2])


# tuple functions

z = (5, 2, 3, 1, 1)

print(z)
print(3 in z)
print(z.index(5))
print(z.count(1))

