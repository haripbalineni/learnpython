# RANGES
# syntax: range(arraystart,arraystop,increment/decrement)
# syntax: range(array)

# prints from 0 to 499
# for n in range(500):
#     print(n)


# prints from 499 to 401
# for n in range(500,400,-1):
#     print(n)

# prints from 3 to 9
# for n in range(3,10):           
#     print(n)

# prints from 3 to 9, incrementing 2
# for n in range(3,10,2):           
#     print(n)


burgers = ['chicken','beef','veg','double','regular','double']

# to Print the values
for n in range(0,len(burgers),1):
    print(n + 1,burgers[n])

# to Print the values in reverse order
# for n in range(len(burgers) -1, -1, -1):  
#     print(n + 1,burgers[n])