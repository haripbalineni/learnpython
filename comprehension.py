#double prize money

#program 1
prizes = [5, 10, 50, 100, 1000]
dbl_prizes = []
for prize in prizes:
    dbl_prizes.append(prize*2)
print(dbl_prizes)

#program 2
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_even_nums = []
for num in nums:
    if(num ** 2) % 2 == 0:
        squared_even_nums.append(num ** 2)
print(squared_even_nums)

#comprehension methods

#program 1
dbl_prizes =  [prize*2 for prize in prizes]
print(dbl_prizes)

#program 2
dbl_prizes = [num ** 2 for num in range(1,11) if (num ** 2) % 2 == 0]
print(dbl_prizes)

