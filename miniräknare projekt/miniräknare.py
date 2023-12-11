def addera(x, y):
    return round(x + y, 2)

def subtrahera(x, y):
    return round(x - y, 2)

def multiplicera(x, y):
    svar = round(x * y, 2)
    return svar

def dividera(x, y):
    if y == 0:
        return "Kan inte dividera med noll"
    return round(x / y, 2)

print("Välj operation.")
print("1. Addera")
print("2. Subtrahera")
print("3. Multiplacera")
print("4. Dividera")

while True:
    val = input("Välj mellan (1/2/3/4): ")

    if val in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Skriv in första numret: "))
            num2 = float(input("Skriv in andra numret: "))
        except ValueError:
            print("Felaktig input. Ange ett nummer.")
            continue

        if val == '1':
            print(num1, "+", num2, "=", addera(num1, num2))

        elif val == '2':
            print(num1, "-", num2, "=", subtrahera(num1, num2))

        elif val == '3':
            print(num1, "*", num2, "=", multiplicera(num1, num2))

        elif val == '4':
            resultat = dividera(num1, num2)
            print(num1, "/", num2, "=", resultat)

        nästa_berkäning = input("Låt oss göra nästa beräkning? (Ja eller Nej): ")
        if nästa_berkäning == "nej":
            print("Tack för att du har testat min miniräknare!")
            break
    else:
        print("Felaktig input")
