class Circle:

    def __init__(self,radius):
        self.radius = radius

    def calculateArea(self):
        area =  (22 / 7 ) * self.radius ** 2  
        return f'The area of circle is {area}'

