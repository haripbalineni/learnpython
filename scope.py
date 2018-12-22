# VARIABLE SCOPE

myName = 'Hari'

def PrintMyName():
  global myName  #redefining global variable
  myName = 'Prakash'
  print(myName)


PrintMyName()
print(myName)