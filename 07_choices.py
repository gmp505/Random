# ================================================================
#  Funkcija: random.seed()
#  Apraksts: Iestata pseidonejaushuma generators sakumvertibumu.
#             Vienada seed -> vienadi "nejausho" skaitlu rezultati.
#  Fails:    01_seed.py
# ================================================================
import random

random.seed(42)
print("Seed=42, pirmie 5 skaitli:")
for i in range(5):
    print(f"  {random.randint(1,100)}", end="")
print()

random.seed(42)
print("Atkartojam seed=42 (identisks rezultats):")
for i in range(5):
    print(f"  {random.randint(1,100)}", end="")
print()

random.seed(99)
print("Seed=99 (cits rezultats):")
for i in range(5):
    print(f"  {random.randint(1,100)}", end="")
print()
