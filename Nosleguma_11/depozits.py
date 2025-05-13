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

def aprekinasana(): #izveidot atiecīgo materiālu ciparu notiek summas un kopsummas aprēķināšana
    kopsumma = 0

    while True:
        try:
            materials = int(input("Ievadiet materiālu (1 - Plastmasa, 2 - Skārdene, 3 - Stikla): ")) # Tiek pieprasīts ievadīt materiāla tipu, ja tiek ievadits materiala cipariņš kas netiek piedāvāts, kommanda pieprasa ievadīt pareizu materiāla veidu.
            if materials not in materialuVeidi:
                print("Ievadiet pareizu pudeļu materiālu!")
                continue
        except ValueError:
            print("Ievadi skaitli 1, 2 vai 3")
            continue    

        try:
            Skaits = int(input("Cik pudeles nodosiet?")) # Depozīta nododot jāievada pudeļu skaits cik tiek nodots, ja skaits ir negatīvs progrāma liek skaitli ievadīt atkārtoti.
            if Skaits <= 0:
                print("Ievadiet pozitīvu skaitu!")
                continue
        except ValueError:
            print("Lūdzu ievadiet skaitli!")
            continue

        depozits = {}
        nodosanas_laiks = str(datetime.now().replace(second=2, microsecond=0))
        cena = materialuVeidi[materials]
        summa = cena * Skaits
        kopsumma += summa

        depozits["Nodošanas laiks"] = nodosanas_laiks
        depozits["Materials"] = materials
        depozits["Skaits"] = Skaits
        depozits["Summa"] = summa

        visiDati["saraksts"].append(depozits)   
        visiDati["kopsumma"] += summa
        materialusumma[materials] = materialusumma.get(materials, 0) + summa

        velreiz = input("Vai tev vēl ir depozīts?(J/N): ").capitalize() # Komanda piedāvā nodot vēl depozītu neapturot iepriekšējo nodoto materiālu summu ja izvelies J, proggrama pieprasa ievadīt materiālu un skaitu ja uzspied N, kommanda parāda cik depozīta atmaksa tev pienākās.
        if velreiz == "N":
            print(f"Depozīta atmaksa: {round(kopsumma, 2)} EUR")
            break
        if velreiz == "J":
            continue
        else:
            print("Ja vēlies turpināt nodot depozītu, Izvēlies J - Jā vai N - nē")

    dati = json.dumps(visiDati, indent=4, ensure_ascii=False)
    with open("Nosleguma_11\depozita_dati.json", "w", encoding="utf-8") as datne:
        datne.write(dati)

aprekinasana()