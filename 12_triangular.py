# ================================================================
#  Funkcija: random.choices(seq, weights=None, k=1)
#  Apraksts: Atgriez k elementus AR atkartoshanos.
#             Var norādit svertās varbūtibas (weights).
#  Fails:    07_choices.py
# ================================================================
import random

random.seed(11)
moneta = ["GALVA", "ASTE"]
print("Monetas mesana 10 reizes:")
print(" ", random.choices(moneta, k=10))

# Ar svertajam varbūtibam
balvas = ["Lielbalva", "Videja balva", "Maza balva", "Nekas"]
svari  = [1, 5, 20, 74]
print("\n100 loterijas bilete (svert. varbūtibas 1:5:20:74):")
rezultati = random.choices(balvas, weights=svari, k=100)
for b in set(balvas):
    print(f"  {b:15s}: {rezultati.count(b)}x")
