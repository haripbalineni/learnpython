
# Sort is to sort the alphabets and numbers:
# A..Z..a..Z
# numbers in incremental order

# SET is used to remove duplicates

family = {}

while True:
    name = input("Enter family member name : ")
    age = int(input("Enter family member age : "))

    if name in list(family.keys()):
        print('name already exists')
    else:
        family[name] = age

    val = input("Do you want to add another member ? (y/n) :")
    
    if val == 'y':
        continue
    else:
        break


def DisplayDistinctDictValues(dict): 
    for  val in set(dict.values()):
        print(f'member age is {val}')

def DisplayDistinctDictSortedValues(dict): 
    for  val in sorted(set(dict.values())):
        print(f'member age is {val}')
 


DisplayDistinctDictValues(family)
DisplayDistinctDictSortedValues(family)

