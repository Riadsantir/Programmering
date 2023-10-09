'''
import random
# [0.0, 1.0)
print(random.random())
'''
'''
import random

while True:
    spela = input("Vill du spela? j/n: ")
    
    if spela == 'n':
        print("Vad roligt att du spelade en stund!")
        break

    tarning1 = random.randint(1, 6)
    tarning2 = random.randint(1, 6)
    
    print(tarning1, tarning2)
    
    if tarning1 == tarning2:
        if tarning1 == 6:
            print("sex-vinst")
        else:
            print("steg-vinst")
    else:
        print("förlust")
'''

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

