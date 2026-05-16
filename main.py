# ============================================================
#  random Bibliotēkas "Cheat Sheet" — 15 funkcijas ar piemēriem
#  Autors: [Vārds Uzvārds]   Klase: [Klase]   Datums: 2026
# ============================================================

import random

# ------------------------------------------------------------------
# 1. random.seed() — iestata sakumvertibumu reproducejamiem rezultatiem
# ------------------------------------------------------------------
random.seed(42)
print("1. random.seed(42)   : sekla iestatita")
# Izmantojums: testesana un debugosana, lai katrreis iegitu vienados
# "nejausos" skaitlus.

# ------------------------------------------------------------------
# 2. random.random() — decimalskaitis intervala [0.0, 1.0)
# ------------------------------------------------------------------
r = random.random()
print(f"\n2. random.random()   : {r:.6f}")
# Izmantojums: varbūtibu simulacijas, procenti, normalizacija.

# ------------------------------------------------------------------
# 3. random.randint(a, b) — vesels skaitis no a lidz b (ieskaitot)
# ------------------------------------------------------------------
n = random.randint(1, 100)
print(f"\n3. random.randint()  : {n}  (starp 1 un 100)")
# Izmantojums: kaulinu mesana, loterijas numuri, testa dati.

# ------------------------------------------------------------------
# 4. random.uniform(a, b) — decimalskaitis no a lidz b
# ------------------------------------------------------------------
t = random.uniform(18.0, 30.0)
print(f"\n4. random.uniform()  : {t:.2f}  (starp 18.0 un 30.0)")
# Izmantojums: temperaturas, svara, cenu simulacija.

# ------------------------------------------------------------------
# 5. random.randrange(start, stop, step) — vesels skaitis no diapazona
# ------------------------------------------------------------------
p = random.randrange(0, 100, 10)
print(f"\n5. random.randrange(): {p}  (0, 10, 20, ..., 90)")
# Izmantojums: nejauša sola vertiba, simulacijas ar soli.

# ------------------------------------------------------------------
# 6. random.choice(seq) — nejauši viens elements no secibas
# ------------------------------------------------------------------
krasas = ["sarkana", "zala", "zila", "dzeltena", "violeta"]
k = random.choice(krasas)
print(f"\n6. random.choice()   : '{k}'  no saraksta")
# Izmantojums: nejausas atbildes, spelu lemumi.

# ------------------------------------------------------------------
# 7. random.choices(seq, k=n) — n elementi AR atkartosanos
# ------------------------------------------------------------------
moneta = ["GALVA", "ASTE"]
mesana = random.choices(moneta, k=10)
print(f"\n7. random.choices()  : {mesana}")
# Izmantojums: monetas mesana, loterija ar atliksanu atpakal.

# ------------------------------------------------------------------
# 8. random.sample(seq, k) — k elementi BEZ atkartosanas
# ------------------------------------------------------------------
skaitli = list(range(1, 50))
loto = random.sample(skaitli, 6)
print(f"\n8. random.sample()   : {sorted(loto)}  (loterijas skaitli 1-49)")
# Izmantojums: loterija, nejausu testu jautajumu atlase.

# ------------------------------------------------------------------
# 9. random.shuffle(lst) — samaisa sarakstu uz vietas
# ------------------------------------------------------------------
kartis = ["A", "K", "Q", "J", "10", "9", "8"]
random.shuffle(kartis)
print(f"\n9. random.shuffle()  : {kartis}")
# Izmantojums: karsu sajuksana, jautajumu secibas randomizacija.

# ------------------------------------------------------------------
# 10. random.gauss(mu, sigma) — Gausa (normalais) sadalijums
# ------------------------------------------------------------------
augumi = [round(random.gauss(175, 10), 1) for _ in range(5)]
print(f"\n10. random.gauss()   : {augumi} cm  (vid.=175, sigma=10)")
# Izmantojums: ermena meri, IQ, ekonomiskie modeli.

# ------------------------------------------------------------------
# 11. random.normalvariate(mu, sigma) — normalais sadalijums (alternativa)
# ------------------------------------------------------------------
rez = [round(random.normalvariate(70, 15), 1) for _ in range(5)]
print(f"\n11. normalvariate()  : {rez}  (vid.=70, sigma=15)")
# Izmantojums: atzimu simulacija, merijumu kludas.

# ------------------------------------------------------------------
# 12. random.triangular(low, high, mode) — trisstaura sadalijums
# ------------------------------------------------------------------
cenas = [round(random.triangular(50, 200, 100)) for _ in range(5)]
print(f"\n12. triangular()     : {cenas} EUR  (min=50, max=200, mod=100)")
# Izmantojums: projektu izmaksu novertesana, riska analize.

# ------------------------------------------------------------------
# 13. random.expovariate(lambd) — eksponencialais sadalijums
# ------------------------------------------------------------------
gaid = [round(random.expovariate(1/5), 1) for _ in range(5)]
print(f"\n13. expovariate()    : {gaid} min  (vidēji 5 min)")
# Izmantojums: gaidisanas laika modelesana, serveru slodze.

# ------------------------------------------------------------------
# 14. random.betavariate(alpha, beta) — beta sadalijums [0, 1]
# ------------------------------------------------------------------
varb = [round(random.betavariate(2, 5), 3) for _ in range(5)]
print(f"\n14. betavariate()    : {varb}")
# Izmantojums: varbūtibu un proporciju modelesana (A/B testesana).

# ------------------------------------------------------------------
# 15. random.getrandbits(k) — nejauši k biti (lieliem skaitliem)
# ------------------------------------------------------------------
bits = random.getrandbits(16)
print(f"\n15. getrandbits(16)  : {bits}  (max={2**16-1})")
# Izmantojums: kriptografijas atslegu generesana, UUID veidosana.

print("\n" + "="*60)
print("  Visas 15 random funkcijas demonstretas veiksmigi!")
print("="*60)
