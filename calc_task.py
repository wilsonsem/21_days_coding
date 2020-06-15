import math
l , b, r, P, R, T = 5, 15, 7, 10000, 0.5, 5

#the code below calculates the area of a rectangle
rect_area = l*b
print("The area of the rectangle with length", l , "and breadth", b ,"is:",rect_area,"\n")

#the block of code below calculates the perimeter of the rectangle above
rect_perimeter =2*(l+b)
print("The perimeter of the rectangle with length", l ,"and breadth", b ,"is:",rect_perimeter,"\n")

#the block of code below calculates the area of a circle with given radius
circle_area= math.pi*r*r
print("The area of the circle with radius", r ,"is: %.2f" %circle_area,"\n")

#the block below calculates the Siple Interest on given parameters
SI=(P*R*T)/100
print("The SI(Simple Interest) on principal amount", P ,"at rate", R ,"with time", T ,"is: %.2f" %SI,"\n")


