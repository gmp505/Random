# ================================================================
#  Funkcija: random.betavariate(alpha, beta)
#  Apraksts: Beta sadalijums — atgriez vertibas intervala [0, 1].
#             Alpha un beta parametri nosaka sadalijuma formu.
#  Fails:    14_betavariate.py
# ================================================================
import random

random.seed(88)
print("A/B testeshana — klikshkhu koeficienti (CTR):")
print("  Variant A (alpha=8, beta=92) -> paredzets ap 8%")
ctr_a = [round(random.betavariate(8, 92) * 100, 2) for _ in range(8)]
print(f"  {ctr_a}%")

print("  Variant B (alpha=12, beta=88) -> paredzets ap 12%")
ctr_b = [round(random.betavariate(12, 88) * 100, 2) for _ in range(8)]
print(f"  {ctr_b}%")
