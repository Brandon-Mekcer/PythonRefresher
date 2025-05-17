def areaSquare(side):
    area = side**2
    return area
def perSquare(side):
    perimeter = side*4
    return perimeter
length = int(input("What is the side length of the square? "))
pSquare = perSquare(length)
aSquare = areaSquare(length)
print(f"The area of the square is {aSquare}")
print(f"The perimeter of the square is {pSquare}")