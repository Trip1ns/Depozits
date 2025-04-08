import json
import uuid

visiDati = []
materialuVeidi = {'Plastmasa': 0.1, 'Skardene': 0.2, 'Stikla': 0.5}

try:
    with open("depozita_dati.json", "r", encoding="utf-8") as datne:
        dati = datne.read()
    visiDati = json.loads(dati)
except:
    pass  

materials = input("Ievadiet materiālu (Plastmasa, Skardene, Stikla): ")
Skaits = int(input('Cik pudeles nodosiet? '))

if materials in materialuVeidi:
    depozits = {}
    numurs = str(uuid.uuid4())
    cena = materialuVeidi[materials]
    summa = cena * Skaits
    print(f"Kopējā summa: {summa} EUR")
    depozits["Numurs"] = numurs
    depozits["Materials"] = materials
    depozits["Skaits"] = Skaits
    depozits["Summa"] = summa

    visiDati.append(depozits)

    dati = json.dumps(visiDati, ensure_ascii=False)
    a = f"Nosleguma_11/depozita_dati.json"
    with open(a, "w", encoding="utf-8") as datne:
        datne.write(dati)
else:
    print("Nederīgs materiāla veids! Lūdzu, izvēlieties no: Plastmasa, Skardene, Stikla.")
