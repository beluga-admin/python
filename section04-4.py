# section04-4
# python data type
# dictionary, set

# dictionary : order x, duplicate x, edit o, delete o

# key, value (Json) -> MongoDB
# declaration

a = {'name': 'kim', 'phone': '010-1234-5678', 'birth': '19900101'}
b = {0: 'Hello Python', 1: 'Hello World'}
c = {'arr': [1, 2, 3, 4, 5]}

print(type(a))

print(a['name'])
print(a.get('name'))
print(a.get('address'))
print(c['arr'][1:3])  

a['address'] = 'Seoul'
print(a)
a['rank'] = [1, 2, 3, 4, 5] 
a['rank2'] = (1, 2, 3, 4, 5)
print(a)

# keys, values, items
print(a.keys())
print(list(a.keys()))
temp = list(a.keys())
print(temp[0])

print(a.values())
print(a.items())

# sets : order x, duplicate x
a = set()
b = set([1, 4, 5, 6, 6])
c = set([1, 2, 3, 4, 5])

print(type(a))
print(c)

t = tuple(b)
l = list(b)
print(l)

s1 = set([1, 2, 3, 4, 5])
s2 = set([4, 5, 6, 7, 8])

print(s1.intersection(s2))
print(s1 & s2)

print(s1 | s2)
print(s1.union(s2))

print(s1 - s2)
print(s1.difference(s2))

# set add & remove
s3 = set([1, 2, 3, 4, 5])
s3.add(6)
print(s3)
s3.remove(6)
print(s3)