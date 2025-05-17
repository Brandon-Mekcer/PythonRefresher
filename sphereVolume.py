import math
pi = math.pi
r = input("What is the radius of the sphere? ")
rlist = r.split(" ")
rfloat = float(rlist[0])
rcubed = rfloat**3
volume = (4/3)*pi*rcubed
match rlist[1]:
    case "m":
        measure = "meters"
    case "cm":
        measure = "centimeters"
    case "km":
        measure = "kilometers"
    case "mm":
        measure = "milimeters"
    case "dm":
        measure = "decimeters"
    case "Dm":
        measure = "decameters"
    case _:
        measure = ""
        print("Received unknown unit of measure. Kindly try again!")

print(f"The volume of the sphere is {volume} {measure} cubed.")