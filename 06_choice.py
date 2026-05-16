# ================================================================
#  Funkcija: random.gauss(mu, sigma)
#  Apraksts: Generē nejaushus skaitlus pec Gausa normalā sadalijuma.
#             mu = vidēja vertiba, sigma = standartnovirze.
#  Fails:    10_gauss.py
# ================================================================
import random

random.seed(44)
print("Skolenu augumi (cm): mu=175, sigma=10")
augumi = [round(random.gauss(175, 10), 1) for _ in range(10)]
print(" ", augumi)
print(f"  Videjais: {sum(augumi)/len(augumi):.1f} cm")

print("\nIQ testa rezultati: mu=100, sigma=15")
iq = [round(random.gauss(100, 15), 1) for _ in range(10)]
print(" ", iq)
print(f"  Videjais: {sum(iq)/len(iq):.1f}")
