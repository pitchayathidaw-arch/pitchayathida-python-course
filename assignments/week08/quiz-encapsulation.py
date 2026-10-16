"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""
class Rectangle:

    def __int__(self , length , width):
        self.__length = length
        self.__width = width

    def getArea(self):
        return f"Area of {self.__width} width and {self.__length} lemgth = {self.__width * self.__length} "

    def getperimeter(self):
        return f"Perimeter of {self.__width} width and {self.__length} lemgth = {2 * (self.__width * self.__length)} "

    def isSquare(self):
        return self.__width == self.__length

myRectangl = Rectangle(5,10)
print(myRectangl.getArea())

myRectangl2 = Rectangle(10 , 10)
print(myRectangl2.isSquare())
print(myRectangl2.isSquare())

print(f"Is square: {myRectangle.isSquare()}")