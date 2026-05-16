# ================================================================
#  Funkcija: random.normalvariate(mu, sigma)
#  Apraksts: Normalais sadalijums — alternativa gauss().
#             Nedaudz lenak, bet drosaka pavedienu darbibai.
#  Fails:    11_normalvariate.py
# ================================================================
import random

random.seed(55)
print("Produktu svari (g): mu=500, sigma=5")
svari = [round(random.normalvariate(500, 5), 1) for _ in range(8)]
for i, s in enumerate(svari, 1):
    nobidijums = s - 500
    print(f"  Produkts {i}: {s}g  (nobidijums: {nobidijums:+.1f}g)")
