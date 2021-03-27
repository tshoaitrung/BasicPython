### the Cylinder class with volume and surface_area
class Cylinder():
    pi = 3.14
    def __init__(self,radius = 1,height = 1):
        self.radius = radius
        self.height = height
    
    def volume(self):
        return self.pi*(self.radius**2)*self.height
    
    def surface_area(self):
        return (2*self.pi*self.radius*self.height) + (2*self.pi*(self.radius**2))
    
    def print_Cylinder(self):
        print('Your Cylinder has radius is {} and height is {}'.format(self.radius,self.height))

###############MAIN##############################
radius = height = 'Wrong'
while radius.isdigit() == False:
    radius = input('Please insert the radius value of your Cylinder: ')
    if radius.isdigit() == True:
        while height.isdigit() == False:
            height = input('Please insert the height value of your Cylinder: ')

your_Cylinder = Cylinder(int(radius),int(height))
your_Cylinder.print_Cylinder()

print('Your Cylinder has the volume is {}'.format(your_Cylinder.volume()))
print('Your Cylinderhas the surface area is {}'.format(your_Cylinder.surface_area()))

