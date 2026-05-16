# ================================================================
#  Funkcija: random.randrange(start, stop[, step])
#  Apraksts: Atgriez nejaushus veselu skaitli no diapazona ar soli.
#             Beigu vertiba NAV ieklauta (ka range()).
#  Fails:    05_randrange.py
# ================================================================
import random

random.seed(1)
print("Paarinati skaitli (0,2,4,...,98):")
print(" ", [random.randrange(0, 100, 2) for _ in range(8)])

print("\nNepaarinati (1,3,5,...,99):")
print(" ", [random.randrange(1, 100, 2) for _ in range(8)])

print("\nDesmitnieki (0,10,...,90):")
print(" ", [random.randrange(0, 100, 10) for _ in range(8)])
