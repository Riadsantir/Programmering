'''
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
'''
