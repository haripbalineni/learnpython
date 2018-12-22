
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


def DisplayAllDictValues(): 
    for key, val in family.items():
        print(f'{key} member age is {val}')

 


DisplayAllDictValues()

