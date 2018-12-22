

# FOR LOOP

# friends = ['sree','manju','kiran','ashok','yog']
# for friend in friends:
#     print(friend)


# for friend in friends[1:3]:
#     print(friend)


# for friend in friends:
#     if friend == 'sree':
#         print(f'{friend} is best friend')
#         break       # to break the loop
#     else:
#         print(friend)


# WHILE LOOP

age = 25
num = 0
while num < age:

    if num < 10:
        num += 1
        continue     
    num += 1
    if num%2 ==0:
         print(f'{num} is even number')
    else:         
        print(f'{num} is odd number') 
        break
               
  
    
