# Section04-2
# Character, Character operation, Slicing

str1 = "I am Boy."
str2 = 'NiceMan'
str3 = ''
str4 = str()

print(len(str1), len(str2), len(str3), len(str4))

escape_str1 = "Do you have a \"big collection\""
print(escape_str1)
escape_str2 = "Tab\tTab\tTab"
print(escape_str2)

# Raw String
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)
raw_s2 = r"\\a\\a"
print(raw_s2)

# multi line string
multi = \
""" 
chracter

multi line

test
"""

print(multi)

# chracter operation
str_o1 = "*"
str_o2 = "abc"
str_o3 = "ABC"
str_o4 = "Niceman"

print(str_o1 * 10)
print(str_o2 + str_o3)
print(str_o2 * 3)
print('a' in str_o4)
print('z' not in str_o4)

# string type convert
print(str(10) + 'a')
print(str(10.4) + 'a' + str(20))

# string function
# refer: https://www.w3schools.com/python/python_ref_string.asp

# a = 'niceman'
# b = 'orange'

# print(a.islower())
# print(a.endswith('e'))
# print(a.replace('nice', 'good'))
# print(list(reversed(b)))

# string slicing
a = 'niceman'
b = 'orange'

print(a[0:3])
print(a[0:4])
print(a[0:7])
print(a[0:len(a)])
print(a[:4])
print(b[0:4:2])
print(b[1:-2])
print(b[::-1])






