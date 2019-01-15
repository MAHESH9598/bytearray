"""---> bytearray is one of the class, treated as Sequence Type datatype
--> The purpose of this data type is to organize the data in the range of 0 to 256
--> mutable
--> To convert specified range of values into bytearray datatype we use a predifined function called bytearray()   """

a = [10, 20, 30, 40]
b = bytearray(a)
print(type(b))

for x in b:
    print(x)

"""b[1]=2019
for y in b:
    print(y)"""  # it gives error bcause the value must be in range of 0 to 256

b[1] = 19
for y in b:
    print(y)

print(b)
print(type(b))

cb = bytes(b)
print(type(cb))

