'''
svar = input("vad heter Norges huvudstad? ")
while svar != "oslo": 
    svar = input("fel, testa igen: ")
print ("Rätt")
'''
'''
svar = input("Gissa talet: ")
while svar != "4":
    svar = input("Du gissade fel. Gissa på ett annat tal. ")
print ("Rätt")
'''
'''
svar = int(input("Gissa talet: "))
antal_svar = 1
while svar != "42":
    if svar < 42: 
     print("för litet ")
    if svar > 42: 
     print("för stort ")
svar = int(input("Gissa talet: "))
antal_svar += 1
print("Du behövde {antal_svar} gissningar för att hitta rätt svar.")
'''
'''
antal_svar = 1

while True:
    svar = int(input("Gissa talet: "))
    
    if svar < 42:
        print("För litet")
    elif svar > 42:
        print("För stort")
    else:
        break 

    antal_svar += 1

print(f"Du behövde {antal_svar} gissningar för att hitta rätt svar.")
'''
antal_gissningar = 3
rätt_svar = 42

for antal_svar in range(1, antal_gissningar + 1):
    svar = int(input("Gissa talet: "))
    
    if svar < rätt_svar:
        print("För litet")
    elif svar > rätt_svar:
        print("För stort")
    else:
        print(f"Grattis! Du hittade rätt svar ({rätt_svar}) på försök {antal_svar}.")
        break
else:
    print(f"Tyvärr, du har använt alla {antal_gissningar} gissningar. Det rätta svaret var {rätt_svar}.")
