import random

def kasta_tärning():
    return random.randint(1, 6)
tärningskast = [kasta_tärning() for _ in range(5)]
antalet_ettor = tärningskast.count(1)
print(f"Antalet ettor är: {antalet_ettor}")
#newnew#