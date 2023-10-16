# Programmering
Loggbok 
=========================

23 09 21 
----------------
Gjorde:
### 7070 slumptal
Fil: 7070 slumptal.py

Exempel:

import random

saldo = 0

print("Välkommen att kasta tärning")
print("Ett spel kostar 1 krona")
print("Vinstplan:")
print("två lika - 3 kr")
print("en sexa - 5 kr")
print("stege - 1 kr")

while True:
    val = input("Välj spela (s), sätt in pengar (i), eller avsluta (a): ")

    if val == 'a':
        print("Vad roligt att du spelade en stund!")
        break
    elif val == 'i':
        insattning = int(input("Ange belopp att sätta in: "))
        saldo += insattning
        print(f"Att spela för: {saldo}")
    elif val == 's':
        if saldo < 1:
            print("Du har inte tillräckligt med pengar.")
        else:
            saldo -= 1
            tarning1 = random.randint(1, 6)
            tarning2 = random.randint(1, 6)

            print(tarning1, tarning2)

            if tarning1 == 6 or tarning2 == 6:
                print("sex-vinst + 5kr")
                saldo += 5
            elif tarning1 == tarning2:
                print("två lika + 3 kr")
                saldo += 3
            elif (tarning1 == 1 and tarning2 == 2) or (tarning1 == 2 and tarning2 == 1):
                print("steg-vinst + 1kr")
                saldo += 1
            else:
                print("förlust")

            print(f"Att spela för: {saldo}")

Gick riktigt bra.
Jag har lärt mig många olika saker denna gången, har lärt mig skillnaden mellan vanligt print() och print(f "" ). Att importera random är också en ny sak för mig, men det
väldigt enkelt. Att använda variabel och ge den ett värde som kan ändras på grund av outputen är också väldigt spännande, som i den här gången var {saldo}. 


vecka 39-40
--------------
gjorde 
### 7073 flödesdiagram 
Fil: 7073 flödesdiagram.py

jag kan inte klistra in flödesdiagram här, men koden har jag skrivit. 
exempel :

~~~

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

~~~

Gick riktigt bra.
Har rittat olika flödesdiagram till alla kod som ligger där uppe, ganska enkelt att göra så och man ska använda det innan man börja programmera något projekt, så skulle jag göra i alla fall. While True och att definera, som i detta fall def sten_sax_pase(): är något nytt som jag har lärt mig, .lower också men det var ganska enkelt. 

Vecka 41-42 
----------------
Gjorde:
### 7100 listor
Fil: 7100 listor.py

Exempel:

~~~
import random

# Kasta en sexsidig tärning 10 gånger och spara resultaten i en lista
resultat_lista = [random.randint(1, 6) for _ in range(10)]
resultat_lista.sort()
summa = sum(resultat_lista)
medelvärde = summa / len(resultat_lista)
minsta = min(resultat_lista)
största = max(resultat_lista)
antalet_sexor = resultat_lista.count(6)
vanligaste_valören = max(set(resultat_lista), key = resultat_lista.count)

# Skriv ut resultaten
print("Resultat:", resultat_lista)
print("Sorterat:", resultat_lista)
print("Summa:", summa)
print("Medelvärde:", medelvärde)
print("Minsta:", minsta)
print("Största:", största)
print("Antal sexor:", antalet_sexor)
print("Vanligast:", vanligaste_valören)

~~~

Jag har lärt mig hur man kan använda listor i Python för att spara och hantera resultat. Listor var mycket storre och bredare än vad jag trode innan jag börjar jobba med dem, de kan exempelvis användas för att samla data, som i det här fallet de olika tärningskasten. Jag har även lärt mig hur man kan använda loopar, som en for-loop, för att upprepa en handling flera gånger. I det här exemplet har jag använt en lista för att spara resultaten av tärningskasten, sedan sorterades listan och beräknades summan och medelvärdet.
