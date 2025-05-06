import json
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

visiDati = {"saraksts": [], "kopsumma": 0}
materialuVeidi = {1: 0.1, 2: 0.2, 3: 0.5}  # | 1 - Plastmasa | 2 - Skārdene | 3 - Stikla |
materialusumma = {}

try:
    with open("Nosleguma_11/depozita_dati.json", "r", encoding="utf-8") as datne:
        dati = datne.read()
        visiDati = json.loads(dati)
except:
    pass

root = tk.Tk()
root.title("Depozīta Pudeļu Nodošana")
root.geometry("400x300")

material_var = tk.IntVar()
material_var.set(1)
skaits_var = tk.StringVar()
summary_var = tk.StringVar()

material_label = tk.Label(root, text="Izvēlies materiālu:")
material_label.pack()

material_options = {
    "Plastmasa": 1,
    "Skārdene": 2,
    "Stikla": 3
}

material_menu = tk.OptionMenu(root, material_var, *material_options.values())
material_menu.pack()


skaits_label = tk.Label(root, text="Cik pudeles nodosiet?")
skaits_label.pack()

skaits_entry = tk.Entry(root, textvariable=skaits_var)
skaits_entry.pack()

def submit():
    try:
        material = material_var.get()
        skaits = int(skaits_var.get())
        if skaits <= 0:
            raise ValueError

        cena = materialuVeidi[material]
        summa = cena * skaits
        kopsumma = summa

        nodosanas_laiks = str(datetime.now().replace(second=2, microsecond=0))

        depozits = {
            "Nodošanas laiks": nodosanas_laiks,
            "Materials": material,
            "Skaits": skaits,
            "Summa": summa
        }

        visiDati["saraksts"].append(depozits)
        visiDati["kopsumma"] += summa
        materialusumma[material] = materialusumma.get(material, 0) + summa

        summary_var.set(f"Depozīta atmaksa: {round(summa, 2)} EUR")

        dati = json.dumps(visiDati, indent=4, ensure_ascii=False)
        with open("Nosleguma_11/depozita_dati.json", "w", encoding="utf-8") as datne:
            datne.write(dati)

    except ValueError:
        messagebox.showerror("Kļūda", "Lūdzu ievadiet pareizu skaitu (pozitīvu skaitli)!")

submit_button = tk.Button(root, text="Iesniegt", command=submit)
submit_button.pack()

summary_label = tk.Label(root, textvariable=summary_var, font=("Arial", 12, "bold"))
summary_label.pack(pady=10)

root.mainloop()
