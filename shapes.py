from cgi import print_arguments
from cmath import pi
# from turtle import circle


class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area_circ(self):
        area_num = pi*(self.radius*self.radius)
        print(  f"{area_num} is your circles area" )

    def circum_circ(self):
        circ_perimeter = pi*(self.radius+self.radius)
        print(f"Your circles perimetre is {circ_perimeter} ")
    
class Square:
    def __init__(self,a):
        self.a = a 

    def area_square(self):
        square_sides = self.a * self.a        
        return square_sides

    def square_perimeter(self):
        perimeter= 4*(self.a)
        return perimeter
    
class Rectangle:
    def __init__(self,width,length):
        self.width = width
        self.length = length

    def area_rectangle(self):
        total_area = self.length * self.width
        return total_area
    
    def rectangle_perimeter(self):
        perimeter = 2*(self.width + self.length)
        return perimeter

class Sphere:
    def __init__(self,r):
        self.r = r
    
    def surface_area (self):
        A = 4* pi(self.r * self.r)
        return A
    
    def sphere_volume(self):
        volume = 4/3*pi*(self.r **3)
        return volume