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

def aprekinasana():
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

            visiDati.append(depozits)

        velreiz = input("Vai tev vēl ir depozīts?(J/N)").capitalize()   
        if velreiz == "J":
            pass
        elif velreiz =="N":
            print(f"Depozīta atmaksa:{kopsumma}")
            break
        else:
            input("Vai tev vēl ir depozīts?(J/N)")

        dati = json.dumps(visiDati, ensure_ascii=False)
        a = f"Nosleguma_11/depozita_dati.json"
        with open(a, "w", encoding="utf-8") as datne:
            datne.write(dati)
aprekinasana()