# ================================================================
#  Funkcija: random.triangular(low, high, mode)
#  Apraksts: Trisstaura sadalijums — visticamaka vertiba ir "mode".
#             Lieliski projektu laika/izmaksu noverteshanai.
#  Fails:    12_triangular.py
# ================================================================
import random

random.seed(66)
print("Projekta laika novertejums (dienas):")
print("  Optimistisks: 5  |  Visticamak: 10  |  Pesimistisks: 25")
laiki = [round(random.triangular(5, 25, 10), 1) for _ in range(8)]
print("  Simulacija:", laiki)
print(f"  Videjais  : {sum(laiki)/len(laiki):.1f} dienas")

print("\nPreces cenu novertejums (EUR):")
print("  min=50  |  mod=120  |  max=300")
cenas = [round(random.triangular(50, 300, 120)) for _ in range(8)]
print("  Simulacija:", cenas)
