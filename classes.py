# CLASS attributes and methods are divided into two groups 
# 1. instance level
# 2. class level

#instance can call classmethods ,class directly cannot call instance methods

class Planet:
    shape ='round'   #class level attribute


    # Constructor
    # self indicates instance
    def __init__(self,name,gravity):
        self.name = name
        self.gravity = gravity

    # instance level method
    def instanceLevelMethod(self):
        return f'{self.name} gravity is {self.gravity}'


    # class leve method
    @classmethod
    def classlevelmethod(nau):
        return f'all planets are {nau.shape} in shape'


oPlanet = Planet('Mars',6)

print(oPlanet.instanceLevelMethod())
print(oPlanet.classlevelmethod())

print(Planet.classlevelmethod())
# print(Planet.instanceLevelMethod()) # cant access instance level methods and attributes


