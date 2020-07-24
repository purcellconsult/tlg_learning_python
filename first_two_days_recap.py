
# variable

x = 5
y = 1.2636
z = 'python'

print(x)  # displays the output to console
print(y)
print(z)


# how do we determine the type of a variable?

print(type(x))
print(type(y))
print(type(z))

# basic mathematical operators
# + - * / () ** % //

print(5 // 3)  # 1 // is the floor operator

a = (5 * 9 / 3) + 10 ** 2  # shows how to use
print(a)

# strings

a = 'python'                        # single quote
b = "JavaScript"                    # double quotes
c = """This is a docstring"""        # triple quotes, or docstring

# ways to format a string in python
print('The language is', a)                     # can use comma to format strings
print('{0} and {1} are programming languages'.format(a.capitalize(), b))  # Can put the indexes in the string
print('{1} and {0} are programming languages'.format(a.capitalize(), b))  # can change the order of the indexes in string

# the f-string
a, b, c = .28372993, 10323.288, 50

# 5 x 100 = 500!

print(f'{a} x {b} = {a * b}!')

# c-style programing
# printf() function in C-programing
print('%d * %d = %d' % (5, 5, 5 * 5))

# properties of strings

# indexing

x = 'football'
y = 'basket ball'

print(x[0])  # f
print(x[4])  # b
print(x[-1]) # l
print(x[len(x) - 1]) # l

# slice
# string[start:stop:skip]

print(x[0:4])  # 'foot'
print(x[4:])   # ball
print(x[4:100]) # ball
print(x[::])  # football
print(x[:5])  # footb
print(x[::1]) # football
print(x[::2]) # fobl
print(x[::-1]) # llabtoof
print(x[5:-1])

# 4 builtin data structures in python
# data structures store and organize data

# list
# -----
# mutable data structure: can modify it
# index list like a string
# a list can be sliced like a string
# append --> adds element to the end of list
# pop   --> removes last element of list
# extend --> adds another list to the list
# sort --> sorts list in ascending order by default
# list are great when we need to rapidly modify a data structure
# list has index and elements. Indexes are integers that map to values. An element is data

x = []  # empty list
x.append(10)  # adds 10
x.append(20)  # adds 20 at end of list
x.append(30)  # adds 30 at end
x.append(40)  # adds 40 at end
print(x)      # [10, 20, 30, 40]

# remove 40 from the x
x.pop()  # removes 40
x.pop()  # removes 30
print(x) # [10, 20]
x.extend([30, 40, 50, 60])
print(x)  # [10, 20, 30, 40, 50, 60]

# tuple
# -----
# immutable data structures
# once created in memory, can't reassign
# use tuple when you want to store data that won't change
# tuple is more memory efficient than list
# has limited functionality compared to list
# tuples are great when there's a relationship between data

laptop = ('apple', 'dell', 'hp', 'sony', 'lenovo')

# index
print(laptop[0])  # apple
print(laptop[-1])  # lenovo

# slice tuple
print(laptop[2:])  # (hp, sont, lenovo)

# list indexes can be reassigned
odds = [1, 3, 5]
odds[2] = 7  # [1, 3, 7]

evens = (2, 4, 6)
# evens[0] = 10  This results in an error, tuples are immutable!

# dictionaries
# ------------
# key/value mappings
# dictionaries index data using keys
# use when you need to represent data in a map
# example of dictionaries in action is JSON

military = {'a': ['army', 'airforce'], 'c ': 'coast guard', 'n': 'navy', 'm': 'marines'}

# keys
print(military.keys())

# values
print(military.values())

# get specific value
print(military['a']) # [army', 'airforce]

# get method
print(military.get('m'))  # marines

# reassignment, a benefit of using subscript notation
military['n'] = 'Navy'
print(military)

# set
# ---
# containers for unique items only

a = {1, 1, 2, 5, 10}  # {1, 2, 10, 5}
print(a)
