upperCase = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lowerCase = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
character = input("Please input a character: ")
while character not in upperCase and character not in lowerCase:
    character = input("Please input an alphabetical character: ")
if character in upperCase:
    print("Your character is upper case!")
else:
    print("Your character is lower case!")
