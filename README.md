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
