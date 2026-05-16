# ================================================================
#  Funkcija: random.uniform(a, b)
#  Apraksts: Atgriez nejaushus decimalskaiti no a lidz b.
#             Atshkiras no random() — var norādit jebkuru diapazonu.
#  Fails:    04_uniform.py
# ================================================================
import random

random.seed(3)
print("Temperaturu simulacija (18.0 - 28.0 C):")
for diena in ["P", "O", "T", "C", "Pk", "S", "Sv"]:
    t = random.uniform(18.0, 28.0)
    print(f"  {diena}: {t:.1f} C")

print("\nSvara merijumi (65.0 - 68.0 kg):")
svari = [round(random.uniform(65.0, 68.0), 2) for _ in range(5)]
print(" ", svari)
