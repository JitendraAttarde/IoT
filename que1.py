#  Write a Python Program find an area of a rectangle and perimeter of the rectangle.

length=float(input("Enter length of rectangle :"))
breadth=float(input("Enter breadth of rectangle :"))

area= length * breadth

perimeter = 2*(length + breadth)

print(f"Area of rectangle = {area}")

print(f"perimeter of rectangle = {perimeter}")