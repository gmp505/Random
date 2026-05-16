# ================================================================
#  Funkcija: random.shuffle(lst)
#  Apraksts: Samaisa sarakstu uz vietas (maina pasu sarakstu).
#             Neatgriez nekadu vertibumu — maina originalos datus.
#  Fails:    09_shuffle.py
# ================================================================
import random

random.seed(33)
kartis = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
print("Kartis pirts samaishanas:")
print(" ", kartis)

random.shuffle(kartis)
print("\nKartis pec samaishanas:")
print(" ", kartis)

print("\nPirmās 5 kartis (izdalishana):")
print(" ", kartis[:5])
