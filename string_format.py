# format string

num1 = 10.236112321321
num2 = 23.36945645


#PREVIOUS

# print('num1 is',num1,'and num2 is',num2)

#FORMAT METHOD

# print('num1 is {0} and num2 is {1}'.format(num1,num2))
# print('num1 is {0} \nnum2 is {1}'.format(num1,num2))        #next line
# print('num1 is {0:.4} \nnum2 is {1:.5}'.format(num1,num2))  #no of digits to print
# print('num1 is {0:.4f} \nnum2 is {1:.3f}'.format(num1,num2))  #no of decimals to print


#USING F-STRINGS
print(f'num1 is {num1} \nnum2 is {num2}')

print(f'num1 is {num1:.4f} \nnum2 is {num2:.3f}')  #no of decimals to print
