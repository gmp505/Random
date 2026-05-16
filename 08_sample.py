# ================================================================
#  Funkcija: random.choice(seq)
#  Apraksts: Atgriez vienu nejaushus elementu no secibas.
#             Darbojas ar sarakstiem, virknēm, tuple.
#  Fails:    06_choice.py
# ================================================================
import random

random.seed(8)
vardi = ["Anna", "Karlis", "Laura", "Maris", "Nina"]
print("Nejaushs vardu izvele:")
for _ in range(5):
    print(f"  -> {random.choice(vardi)}")

print("\nNejausha burtu izvele no 'ABCDEFG':")
print(" ", "".join(random.choice("ABCDEFG") for _ in range(10)))

virzieni = ["Ziemeli", "Dienvidiem", "Austrumiem", "Rietumiem"]
print(f"\nGlobuss grieshanas virziens: {random.choice(virzieni)}")
