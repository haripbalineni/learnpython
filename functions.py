#FUNCTION

# Function With out Parameters
# def greet():
#     print('Hello World')


# Function With Parameters
# def greet(name,time):
#     print(f'Hello {name}, Good {time}')


# nm = input('Enter your name :')
# tm = input('Enter time :')

# greet(nm,tm)



# Function With default Parameters
# def greet(name = 'Hari',time = 'Day'):
#     print(f'Hello {name}, Good {time}')


# # nm = input('Enter your name :')
# # tm = input('Enter time :')

# # greet(nm,tm)
# greet(name="Prakash")
# # greet()


#FUNCTION TO CALCULATE AREA 
# 
def area(radius):
    return (3.142) * radius ** 2

def volume(area,length):
    return area * length

iRadius = int(input('Enter radius to calcularte area :')) 
iLength= int(input('Enter length to calcularte volume :')) 

print(f'The area of circle is {area(iRadius)}')
print(f'The volume of cylinder is {volume(area(iRadius),iLength)}')
