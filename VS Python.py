'''
i = 11
while i >= 2:
    print(i)
    i = i - 3
print("klar")
'''

antal_heltal = int(input("Hur många heltal vill du ha? "))

# Läs in det minsta talet i serien
minsta_tal = int(input("Vilket är det minsta talet i serien? "))

# Skriv ut de önskade heltalen
print("Svar:", end=" ")

# Använd en slinga för att generera och skriva ut heltalen
for i in range(minsta_tal, minsta_tal + antal_heltal):
    print(i, end=", ")