# ================================================================
#  Funkcija: random.getrandbits(k)
#  Apraksts: Atgriez nejaushus veselu skaitli ar k bitiem.
#             Izmanto kriptografiskam operacijam un UUID.
#  Fails:    15_getrandbits.py
# ================================================================
import random

random.seed(0)
print("Bitu skaits | Maksimalas vertibas | Piemers")
print("-" * 55)
for bits in [8, 16, 32, 64, 128]:
    maks = 2**bits - 1
    piem = random.getrandbits(bits)
    print(f"  {bits:3d} biti  | {maks:>20d} | {piem}")

print("\n16-bitu token genereshana (5 gabali):")
tokeni = [hex(random.getrandbits(16))[2:].zfill(4).upper() for _ in range(5)]
print("  Tokeni:", "-".join(tokeni))
