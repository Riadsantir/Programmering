'''
tal = int(input("Mata in ett tal: "))

if tal < 0:
    print("Tal mindre än 0 är negativa.")
elif 0 <= tal <= 9:
    print("Det är ensiffriga tal.")
elif 10 <= tal <= 99:
    print("Det är tvåsiffriga tal.")
elif 100 <= tal <= 999:
    print("Det är tresiffriga tal.")
else:
    print("Det är minst fyrsiffriga tal.")
'''
'''
gissning = int(input("Gissa ett tal: "))
while gissning != 4:
    print("Du gissade fel. Gissa på ett annat tal.")
    gissning = int(input("Gissa ett tal: "))
print("Du gissade rätt.")
'''
'''
tal = int(input("Ange ett tal: "))
antal_gissningar = 0
while tal != 42:
    antal_gissningar += 1
    if tal < 42:
        print("För litet")
    elif tal > 42:
        print("För stort")
    tal = int(input("Ange ett tal: "))
print(f"Du behövde {antal_gissningar} gissningar för att hitta rätt svar.")
'''
import random

def sten_sax_pase():
    spelare = input("Välj sten, sax eller påse: ").lower()
    datorn = random.choice(["sten", "sax", "påse"])

    print(f"Datorn valde: {datorn}")

    if spelare == datorn:
        print("Oavgjort!")
    elif spelare == "sten":
        if datorn == "sax":
            print("Spelaren vinner!")
        else:
            print("Datorn vinner!")
    elif spelare == "sax":
        if datorn == "sten":
            print("Datorn vinner!")
        else:
            print("Spelaren vinner!")
    elif spelare == "påse":
        if datorn == "sten":
            print("Spelaren vinner!")
        else:
            print("Datorn vinner!")
    else:
        print("Ogiltigt val. Försök igen.")

while True:
    sten_sax_pase()
    fortsatt = input("Vill du spela igen? (ja/nej): ").lower()
    if fortsatt != "ja":
        break

print("Tack för att du spelade!!")
