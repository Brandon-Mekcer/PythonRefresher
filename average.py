array = []
while len(array) < 5:
    value = int(input("Please input a value: "))
    array.append(value)
print("Thank you!")
sum = 0
for i in array:
    sum += float(i)
avr = sum / len(array)
print(f"The average of your 5 values is {avr}")