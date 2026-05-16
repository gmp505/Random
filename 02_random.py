# ================================================================
#  Funkcija: random.sample(population, k)
#  Apraksts: Atgriez k nejaushus elementus BEZ atkartoshanas.
#             Katrs elements var paradities tikai vienu reizi.
#  Fails:    08_sample.py
# ================================================================
import random

random.seed(22)
skaitli = list(range(1, 50))
print("Loto skaitli (6 no 1-49):")
print(" ", sorted(random.sample(skaitli, 6)))

jautajumi = [f"Jautajums {i}" for i in range(1, 21)]
print("\nNejausha testa izvele (5 no 20):")
print(" ", random.sample(jautajumi, 5))

dalibnieki = ["Anna","Karlis","Laura","Maris","Nina","Oskars","Petra","Ruta"]
print("\nNejausha komandu sadale (3+3+2):")
komanda1 = random.sample(dalibnieki, 3)
atlikushie = [d for d in dalibnieki if d not in komanda1]
komanda2 = random.sample(atlikushie, 3)
komanda3 = [d for d in atlikushie if d not in komanda2]
print(f"  Komanda 1: {komanda1}")
print(f"  Komanda 2: {komanda2}")
print(f"  Komanda 3: {komanda3}")
