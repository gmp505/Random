# ================================================================
#  Funkcija: random.randint(a, b)
#  Apraksts: Atgriez nejaushus veselu skaitli no a lidz b (IESKAITOT abus).
#             Atshkiras no randrange — beigu robezhna IR ieklauta.
#  Fails:    03_randint.py
# ================================================================
import random

random.seed(5)
print("Kaulinu simulacija (1-6), 10 metieni:")
metieni = [random.randint(1, 6) for _ in range(10)]
print(" ", metieni)

print("\nKaulinhu statistika no 1000 metieniem:")
saskaitijums = {i: 0 for i in range(1, 7)}
for _ in range(1000):
    saskaitijums[random.randint(1, 6)] += 1
for skaitlis, skaits in sorted(saskaitijums.items()):
    bar = "#" * (skaits // 10)
    print(f"  {skaitlis}: {skaits:4d} {bar}")
