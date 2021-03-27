### Line class methods to accept corrfinates as a pair of tuples and return the slope and distance of the line
import math # to use square root
class Line():
    def __init__(self,x1 = 0,y1 = 0,x2 = 1,y2 = 1): #LINE (x1,y1) (x2,y2)
        self.point1 = (x1,y1) #the horizontal 
        self.point2 = (x2,y2) #the vertical

    def distance(self):
        return math.sqrt((self.point2[0]-self.point1[0])*(self.point2[0]-self.point1[0]) + (self.point2[1]-self.point1[1])*(self.point2[0]-self.point1[0]))
        
    def slope(self):
        return abs((self.point2[1]-self.point1[1])/(self.point2[0]-self.point1[0]))
        
    def print_line(self):
        print('This line inludes two point: start point is ({},{}) and end point is ({},{})'.format(self.point1[0],self.point1[1],self.point2[0],self.point2[1]))

##################MAIN############################
x1 = y1 = x2 = y2 = 'WRONG'
while x1.isdigit() == False:
    x1 = input('Insert the value of point 1 - Horizontal: ')
    if x1.isdigit() == True:
        while y1.isdigit() == False:
            y1 = input ('Insert the value of point 1 - Vertical: ')
            if y1.isdigit() == True:
                while x2.isdigit() == False:
                    x2 = input('Insert the value of point 2 - Horizontal: ')
                    if x2.isdigit() == True:
                        while y2.isdigit() == False:
                            y2 = input ('Insert the value of point 2 - Vertical: ')
                            
example_line = Line(int(x1),int(y1),int(x2),int(y2))
example_line.print_line()

print('The length of your line is {}'.format(example_line.distance()))
print('The slope of your line is {}'.format(example_line.slope()))
