import json
from datetime import datetime
import tkinter


tagad = datetime.now()
apalots = tagad.replace(second=2, microsecond=0)

visiDati = {"saraksts": [], "kopsumma": 0}
materialuVeidi = {1: 0.1, 2: 0.2, 3: 0.5} # | 1 - Plastmasa | 2 - Skārdene | 3 - Stikla |
materialusumma = {}
try:
    with open("Nosleguma_11\depozita_dati.json", "r", encoding="utf-8") as datne:
        dati = datne.read()
        visiDati = json.loads(dati)
except:
    pass

def aprekinasana():
    kopsumma = 0

    while True:
        try:
            materials = int(input("Ievadiet materiālu (1 - Plastmasa, 2 - Skārdene, 3 - Stikla): ")) # Ievada pudeles materiālu
            if materials not in materialuVeidi:
                print("Ievadiet pareizu pudeļu materiālu!")
                continue
        except ValueError: # Kļūdu pārbaude
            print("Ievadi skaitli 1, 2 vai 3")
            continue    

        try:
            Skaits = int(input("Cik pudeles nodosiet?")) # Ievada pudeļu skaitu
            if Skaits <= 0:
                print("Ievadiet pozitīvu skaitu!")
                continue
        except ValueError: # Kļūdu pārbaude
            print("Lūdzu ievadiet skaitli!")
            continue

        depozits = {}
        nodosanas_laiks = str(datetime.now().replace(second=2, microsecond=0))
        cena = materialuVeidi[materials]
        summa = cena * Skaits # Tiek aprēķināta summa par vienu ierakstu
        kopsumma += summa # Tiek aprēķināta kopsumma par n-ierakstiem

        depozits["Nodošanas laiks"] = nodosanas_laiks #atslēgas
        depozits["Materials"] = materials #atslēgas
        depozits["Skaits"] = Skaits #atslēgas
        depozits["Summa"] = summa #atslēgas

        visiDati["saraksts"].append(depozits) # Dati tiek aizsūtīti uz JSON datni
        visiDati["kopsumma"] += summa # Kopsumma tiek saskaitīta un aizūtīta uz JSON datni
        materialusumma[materials] = materialusumma.get(materials, 0) + summa # Ievades kopsumma tiek saskaitīta ar ierpiekšējo ierakstu kopsummām

        velreiz = input("Vai tev vēl ir depozīts?(J/N): ").capitalize() # Programma prasa vai vēlaties nodot vēl depozītu
        if velreiz == "N":
            print(f"Depozīta atmaksa: {round(kopsumma, 2)} EUR")
            break
        if velreiz == "J":
            continue
        else:
            print("Ja vēlies turpināt nodot depozītu, Izvēlies J - Jā vai N - nē") # Kļūdu pārbaude

    dati = json.dumps(visiDati, indent=4, ensure_ascii=False)
    with open("Nosleguma_11\depozita_dati.json", "w", encoding="utf-8") as datne:
        datne.write(dati)

aprekinasana()