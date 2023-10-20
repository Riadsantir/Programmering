# tal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# primtal = [2, 3, 5, 7, ]

# 4 går bort ty delbart med 2
# 6 går bort ty delbart med 2 och 3
# 8 går bort ty delbart med 2 och 4

def är_primtal(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
# Detta eftersom alla primtal större än 3 är av formen 6k ± 1, där k är ett heltal.
primtal_lista = [n for n in range(2, 100) if är_primtal(n)]

print("Primtalen under 100 är:")
print(primtal_lista)
