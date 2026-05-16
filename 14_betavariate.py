# ================================================================
#  Funkcija: random.expovariate(lambd)
#  Apraksts: Eksponencialais sadalijums.
#             lambd = 1/videjais_laiks.
#             Modelē gaidishanas laiku starp notikumiem.
#  Fails:    13_expovariate.py
# ================================================================
import random

random.seed(77)
videjais_gaidishanas_laiks = 5  # minutēs
lambd = 1 / videjais_gaidishanas_laiks

print(f"Klientu gaidishanas laiki (vidēji {videjais_gaidishanas_laiks} min):")
laiki = [round(random.expovariate(lambd), 2) for _ in range(10)]
for i, t in enumerate(laiki, 1):
    print(f"  Klients {i:2d}: {t:.2f} min")
print(f"  Faktiskais videjais: {sum(laiki)/len(laiki):.2f} min")
