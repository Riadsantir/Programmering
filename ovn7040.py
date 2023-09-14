'''
namn = input("Vad heter du?")
print("Hej", namn, "!")
favorite = input("What is your favourite color?")
print (namn, "your", "favorite", "color", "is", favorite)
'''
'''
name = "Alice"
age = 30
print("My name is", name, "and I am", age, "years old.", end=" ")
print("Nice to meet you!")
'''
'''
bredd = float(input("Ange rektangelns bredd: "))
höjd = float(input("Ange rektangelns höjd: "))
area = bredd * höjd
omkrets = 2 * (bredd + höjd)
print("area:", area)
print("omkrets:", omkrets)
'''

text = input("Ange ett ord: ")

if "R" in text or "r" in text:
    if "S" in text:
        print("Riad Santir")
    else:
        print('R gang')
elif "S" in text or "s" in text:
    print("S gang")
else:
    print('No gang')

print('klart')
