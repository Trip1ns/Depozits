import json
from datetime import datetime
import tkinter


visiDati = []
materialuVeidi = {'Plastmasa': 0.1, 'Skardene': 0.2, 'Stikla': 0.5}

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
        materials = input("Ievadiet materiālu (Plastmasa, Skardene, Stikla): ")
        if materials not in materialuVeidi:
            input("Ievadiet pareizu pudeļu materiālu:")
        Skaits = int(input('Cik pudeles nodosiet? '))
        if Skaits < 0:
            int(input("Ievadiet pozitīvu skaitu:"))
            
        if materials in materialuVeidi:
            depozits = {}
            numurs = str(uuid.uuid4())
            cena = materialuVeidi[materials]
            summa = cena * Skaits
            kopsumma += summa
            print(kopsumma)
            depozits["Numurs"] = numurs
            depozits["Materials"] = materials
            depozits["Skaits"] = Skaits
            depozits["Summa"] = summa

        visiDati["saraksts"].append(depozits)   
        visiDati["kopsumma"] += summa
        materialusumma[materials] = materialusumma.get(materials, 0) + summa

        velreiz = input("Vai tev vēl ir depozīts?(J/N)").capitalize()   
        if velreiz == "J":
            continue
        else:
            print("Ja vēlies turpināt nodot depozītu, Izvēlies J - Jā vai N - nē")

    dati = json.dumps(visiDati, indent=4, ensure_ascii=False)
    with open("Nosleguma_11\depozita_dati.json", "w", encoding="utf-8") as datne:
        datne.write(dati)

aprekinasana()