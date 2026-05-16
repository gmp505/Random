# ================================================================
#  Funkcija: random.random()
#  Apraksts: Atgriez nejaushus decimalskaiti intervala [0.0, 1.0).
#             Pamata nejaushuma funkcija — uz to balstitas citas.
#  Fails:    02_random.py
# ================================================================
import random

random.seed(7)
print("5 nejausha decimali [0,1):")
for i in range(5):
    print(f"  {random.random():.6f}")

# Varbūtibas simulacija: 30% iespeja
print("\n1000 eksperimentu — ~30% gadijumu vajadzetu but True:")
skaitits = sum(1 for _ in range(1000) if random.random() < 0.3)
print(f"  True gadijumi: {skaitits}/1000 ({skaitits/10:.1f}%)")
