# Section 02-1
# Python Basics Coding
# Understanding Print Statements

#Basic print statement
print("Hello World")
print('Hello Python')
print("""Hello Python""")
print('''Hello Python''') 

print()

# Seperate print statements
print('T', 'e', 's', 't', sep='')
print('2019', '02', '19', sep='-')
print('niceman', 'google.com', sep='@') 

# end print statement
print('Welcome To', end=' ')
print('the black parade', end=' ')
print('piano notes')
print() # prints a new line

# format print statement
print('{} {}'.format('Hello', 'World'))
print('{} and {}'.format('Hello', 'World'))
print("{0} and {1} and {0}" .format('You', 'Me'))
print("{a} are {b}" .format(a='You', b='Me'))

# %s is string, %d is integer, %f is float
print("%s's favorite number is %d" % ('Eunki', 7)) 

print("Test1: %5d, Price: %4.2f" % (776, 6534.123))
print("Test1: {0: 5d}, Price: {1: 4.2f}" .format(776, 6534.123))
print("Test1: {a: 5d}, Price:{b: 4.2f}" .format(a=776, b=6534.123))

# escape character

# \n new line
# \t tab
# \\ backslash
# \' single quote
# \" double quote
# \a bell
# \b backspace
# \f form feed
# \r carriage return
# \v vertical tab
# \000 null

print("'you'")
print('\'you\'')
print('"you"')
print("""'you'""")
print('\\you\\\n\n')
print('test')
print('\t\t\ttest')



