#!/usr/bin/env python3
# ============================================================
#  random Bibliotēkas Demonstrācijas Programma
#  Lietotājs var izvēlēties un palaist jebkuru no 15 piemēriem.
# ============================================================

import random

def demo_01():
    print("\n[1] random.seed() — reproducejama nejaushtiba")
    random.seed(42)
    print("  Seed=42:", [random.randint(1,100) for _ in range(5)])
    random.seed(42)
    print("  Atkart. :", [random.randint(1,100) for _ in range(5)])

def demo_02():
    print("\n[2] random.random() — decimals [0.0, 1.0)")
    random.seed(1)
    for _ in range(5):
        print(f"  {random.random():.6f}")

def demo_03():
    print("\n[3] random.randint(a, b) — vesels skaitlis")
    random.seed(2)
    print("  Kaulina metieni (1-6):", [random.randint(1,6) for _ in range(10)])

def demo_04():
    print("\n[4] random.uniform(a, b) — decimals diapazona")
    random.seed(3)
    temps = [round(random.uniform(18.0, 28.0), 1) for _ in range(7)]
    dienas = ["P","O","T","C","Pk","S","Sv"]
    for d, t in zip(dienas, temps):
        print(f"  {d}: {t} C")

def demo_05():
    print("\n[5] random.randrange(start, stop, step)")
    random.seed(4)
    print("  Desmitniek.:", [random.randrange(0,100,10) for _ in range(8)])
    print("  Paarinati :", [random.randrange(0,100,2) for _ in range(8)])

def demo_06():
    print("\n[6] random.choice() — viens nejaushs elements")
    random.seed(5)
    vardi = ["Anna","Karlis","Laura","Maris","Nina"]
    for _ in range(5):
        print(f"  -> {random.choice(vardi)}")

def demo_07():
    print("\n[7] random.choices() — n elementi AR atkartoshanos")
    random.seed(6)
    moneta = ["GALVA","ASTE"]
    print("  10 monetu metieni:", random.choices(moneta, k=10))
    balvas = ["Lielbalva","Videja","Maza","Nekas"]
    svari  = [1, 5, 20, 74]
    rez = random.choices(balvas, weights=svari, k=50)
    print("  50 loterijas (svert.):")
    for b in balvas:
        print(f"    {b:12s}: {rez.count(b)}x")

def demo_08():
    print("\n[8] random.sample() — k elementi BEZ atkartoshanas")
    random.seed(7)
    loto = sorted(random.sample(range(1, 50), 6))
    print("  Loto 6/49:", loto)
    dalibnieki = ["Anna","Karlis","Laura","Maris","Nina","Oskars"]
    print("  3 nejausha dalibnieki:", random.sample(dalibnieki, 3))

def demo_09():
    print("\n[9] random.shuffle() — saraksta samaishana")
    random.seed(8)
    kartis = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    print("  Pirms:", kartis)
    random.shuffle(kartis)
    print("  Pec  :", kartis)

def demo_10():
    print("\n[10] random.gauss(mu, sigma) — Gausa sadalijums")
    random.seed(9)
    augumi = [round(random.gauss(175, 10), 1) for _ in range(8)]
    print("  Augumi (cm):", augumi)
    print(f"  Videjais: {sum(augumi)/len(augumi):.1f} cm")

def demo_11():
    print("\n[11] random.normalvariate(mu, sigma) — normalais sadalijums")
    random.seed(10)
    svari = [round(random.normalvariate(500, 5), 1) for _ in range(6)]
    print("  Svari (g):", svari)

def demo_12():
    print("\n[12] random.triangular(low, high, mode) — trisstaura sadalijums")
    random.seed(11)
    laiki = [round(random.triangular(5, 25, 10), 1) for _ in range(8)]
    print("  Projekta laiki (dienas):", laiki)
    print(f"  Videjais: {sum(laiki)/len(laiki):.1f}")

def demo_13():
    print("\n[13] random.expovariate(lambd) — gaidishanas laiki")
    random.seed(12)
    laiki = [round(random.expovariate(1/5), 2) for _ in range(8)]
    print("  Gaidishanas laiki (min):", laiki)

def demo_14():
    print("\n[14] random.betavariate(alpha, beta) — beta sadalijums")
    random.seed(13)
    ctr = [f"{random.betavariate(8,92)*100:.2f}%" for _ in range(6)]
    print("  CTR simulacija:", ctr)

def demo_15():
    print("\n[15] random.getrandbits(k) — k-bitu nejauhs skaitlis")
    random.seed(14)
    for bits in [8, 16, 32, 64]:
        print(f"  {bits:3d} biti: {random.getrandbits(bits)}")
    tokeni = [hex(random.getrandbits(16))[2:].zfill(4).upper() for _ in range(5)]
    print("  Token:", "-".join(tokeni))

DEMOS = {
    "1" : ("random.seed()          — reproducejama nejaushtiba", demo_01),
    "2" : ("random.random()        — decimals [0.0, 1.0)",       demo_02),
    "3" : ("random.randint()       — vesels skaitlis [a, b]",    demo_03),
    "4" : ("random.uniform()       — decimals [a, b]",           demo_04),
    "5" : ("random.randrange()     — vesels ar soli",            demo_05),
    "6" : ("random.choice()        — viens elements",            demo_06),
    "7" : ("random.choices()       — n elementi AR atkart.",     demo_07),
    "8" : ("random.sample()        — k elementi BEZ atkart.",    demo_08),
    "9" : ("random.shuffle()       — saraksta samaishana",       demo_09),
    "10": ("random.gauss()         — Gausa sadalijums",          demo_10),
    "11": ("random.normalvariate() — normalais sadalijums",      demo_11),
    "12": ("random.triangular()    — trisstaura sadalijums",     demo_12),
    "13": ("random.expovariate()   — eksponencialais sadalij.",  demo_13),
    "14": ("random.betavariate()   — beta sadalijums",           demo_14),
    "15": ("random.getrandbits()   — k-bitu skaitlis",           demo_15),
    "0" : ("Visi piemeri pec kartas",                            None),
}

def menu():
    print("\n" + "="*60)
    print("   random Bibliotēkas Demonstrācijas Programma")
    print("   Versija 1.0  |  Iebūvēta Python bibliotēka")
    print("="*60)
    for k, (nos, _) in DEMOS.items():
        print(f"  [{k:>2}] {nos}")
    print("\n  [Q]  Iziet")
    print("-"*60)

def main():
    while True:
        menu()
        izvele = input("  Tavs ievads: ").strip().upper()
        if izvele == "Q":
            print("\n  Uz redeshanos!\n")
            break
        elif izvele == "0":
            for k, (_, fn) in DEMOS.items():
                if k != "0": fn()
        elif izvele in DEMOS and DEMOS[izvele][1]:
            DEMOS[izvele][1]()
        else:
            print("  Kludaina izvele. Ievadi 1-15, 0 vai Q.")
        input("\n  [Spied Enter, lai turpinatu...]")

if __name__ == "__main__":
    main()
