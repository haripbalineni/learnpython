#filter(function,data)

grades = ['A', 'B', 'C', 'D', 'E', 'F']

def remove_fails(grade):
    return grade != 'F'

#filter
print(list(filter(remove_fails,grades)))

#using comprehension
filterdvals =  [grade for grade in grades if grade != 'F']
print(filterdvals)

