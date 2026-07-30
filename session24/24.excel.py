# =============================================================
# EXCEL  (.xlsx)  cu  openpyxl  -  citire / scriere / formatare
# =============================================================
# In sesiunea 23 am salvat date in CSV si JSON. CSV e util, dar e doar
# text simplu: NU are formatare (font, culori), NU are mai multe foi si
# NU are formule. Cand vrei un RAPORT pe care sa-l deschida cineva in
# Excel, ai nevoie de un fisier .xlsx adevarat.
#
# `openpyxl` e biblioteca standard de facto pentru .xlsx in Python.
# Nu e built-in - se instaleaza o singura data:
#       pip install openpyxl
#
# Termeni (revenim la fiecare mai jos):
#   WORKBOOK = fisierul .xlsx intreg
#   SHEET    = o foaie (tab) din fisier
#   CELL     = o celula (ex: A1, B5)
#   ROW      = rand (1, 2, 3, ...)     COLUMN = coloana (A, B, C, ...)
#
# De ce ai nevoie ca sa intelegi acest fisier (recap):
#   - liste, dictionare, bucle for (sesiunile 5-9)
#   - lucrul cu fisiere pe disc (sesiunea 23)
# =============================================================

import os

from click.formatting import iter_rows
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, PatternFill, Alignment

# Ca la sesiunea 23: un folder local pentru fisierele generate, ca sa le
# poti deschide cu Excel si sa vezi rezultatul.
TMP = "data_s24"
os.makedirs(TMP, exist_ok=True)


# =============================================================
# PARTEA 1 - BAZELE
# =============================================================


# 1. CREARE WORKBOOK  +  foaia activa
# -------------------------------------------------------------
# Workbook() creeaza un fisier Excel "in memorie". El are DEJA o foaie
# activa, accesibila cu  wb.active. Ii putem da un nume.

wb = Workbook()                   # Definesc un fisier Excel
ws = wb.active                    # setam primul sheet active
ws.title = "Useri"                # redenumim sheet/foaia activa
wb.create_sheet("Produse")        # Defineste un sheet nou produse
wb.save("data_s24/new_excel.xlsx")# salvam fisierul Excel cu denumirea new_excel.xlsx

# 2. SCRIERE IN CELULE  -  doua moduri
# -------------------------------------------------------------
# a) prin coordonata (litera+numar), cel mai lizibil:

ws["A1"] = "Nume"
ws['B1'] = "Varsta"
ws['C1'] = "Rol"


# b) prin numere de rand/coloana - utila in bucle (row=1 e PRIMUL rand,
#    NU 0; coloana A = 1):

ws.cell(row=2, column=1, value="Ana")
ws.cell(row=2, column=2, value=28)
ws.cell(row=2, column=3, value="admin")


# 3. append()  -  adauga un RAND intreg la final
# -------------------------------------------------------------
# Cel mai comod cand ai date gata, linie cu linie.

ws.append(["Horia", 30, "sysadmin"])


# 4. SALVARE pe disc  -  wb.save
# -------------------------------------------------------------
# ATENTIE: pana nu apelezi save(), totul e doar in memorie.

wb.save("data_s24/new_excel.xlsx")

# 5. CITIRE  -  load_workbook, foi, dimensiuni
# -------------------------------------------------------------

fisier_excel = load_workbook("data_s24/new_excel.xlsx")

# afisez toate sheeturile din excel
print(fisier_excel.sheetnames)   #['Useri']

ws2 = fisier_excel['Produse']   # deschis sheet/foaia aceasta nu cea activa (prima)
print(ws2.max_row, ws2.max_column) # aflam numarul de randuri si numarul de coloane


ws1 = fisier_excel['Useri']
print(ws1.max_row, ws1.max_column)

# Valoarea unei celule: .value

print(ws1['A2'].value)
print(ws1['B2'].value)

print(ws1.cell(row=3, column=1).value)

# 6. ITERATIE PE RANDURI  -  iter_rows(values_only=True)
# -------------------------------------------------------------
# values_only=True iti da TUPLURI cu valorile (nu obiecte "cell").

for rand in ws1.iter_rows(values_only=True):
    print(rand)


# Sari peste header cu  min_row=2:
for nume, varsta, rol in ws1.iter_rows(min_row=2, values_only=True):
    print(f"{nume}: {varsta} cu roul {rol}")


# =============================================================
# PARTEA 2 - MAI MULTE FOI si FORMATARE
# =============================================================


# 7. MAI MULTE FOI  -  create_sheet
# -------------------------------------------------------------
# Un avantaj mare fata de CSV: un fisier poate avea mai multe foi.

ws_clienti = wb.create_sheet("Clienti")
ws_clienti.append(["Nume", "CUI"])
ws_clienti.append(['Companie1', "123455"])
ws_clienti.append(['Companie2', "777777"])

wb.save("data_s24/new_excel.xlsx")


# 8. FORMATARE  -  font, culoare de fundal, aliniere pe header
# -------------------------------------------------------------
# PROBLEMA: un tabel fara formatare e greu de citit; nu se vede unde e
# header-ul. SOLUTIA: stiluri din openpyxl.styles pe randul de header.

wb3 = Workbook()
ws3 = wb3.active
ws3.title ="Raport"

ws3.append(["Produse", "Pret"])
ws3.append(["laptop", "4000"])
ws3.append(["mouse", "3000"])

wb3.save("data_s24/raport.xlsx")

header_font = Font(bold=True, color="FFFFFF")  # alb, bolduit
header_fill = PatternFill("solid", fgColor="305496")

for cell in ws3[1]:
    cell.font = header_font
    cell.fill = header_fill

# 9. LATIMEA COLOANELOR
# -------------------------------------------------------------

ws3.column_dimensions["A"].width = 18
ws3.column_dimensions["B"].width = 12

wb3.save("data_s24/raport.xlsx")

# 10. FORMULE EXCEL  -  le scrii ca string  "=..."
# -------------------------------------------------------------
# openpyxl NU calculeaza formule; le SALVEAZA ca text, iar Excel le
# evalueaza cand deschizi fisierul.
ws3['B4'] = "=B2+B3"
ws3['B5'] = "=SUM(B2:B3)"

wb3.save("data_s24/raport.xlsx")

# =============================================================
# RECAP / GRESELI FRECVENTE
# =============================================================
# CREARE:
#   wb = Workbook(); ws = wb.active; ws.title = "Foaie"
#   ws["A1"] = ...  /  ws.cell(row, column, value=...)  /  ws.append([...])
#   wb.save("fisier.xlsx")            # OBLIGATORIU ca sa persiste
#
# CITIRE:
#   wb = load_workbook("fisier.xlsx"); ws = wb["Foaie"]  (sau wb.active)
#   for r in ws.iter_rows(values_only=True): ...   (min_row=2 sare header-ul)
#
# FOI: wb.create_sheet("Nume"), wb.sheetnames, wb.remove(ws)
# STIL: Font / PatternFill / Alignment din openpyxl.styles;
#       ws.column_dimensions["A"].width = 18
#
# Greseli frecvente:
#   - randurile/coloanele incep de la 1, NU de la 0.
#   - sa uiti  wb.save(...)  -> modificarile nu ajung pe disc.
#   - sa astepti ca openpyxl sa CALCULEZE formule: nu o face; le pastreaza
#     ca text. Pentru rezultate: data_only=True (si fisier salvat de Excel).
#   - openpyxl lucreaza doar cu .xlsx (nu cu .xls vechi).
#
# =============================================================
# CONCLUZIE
# =============================================================
# openpyxl adauga peste CSV: formatare, mai multe foi si formule.
# Ai nevoie de el cand livrezi RAPOARTE .xlsx catre oameni.
# Fisierele generate sunt in folderul data_s24/ - deschide-le in Excel.
# =============================================================
print(f"[final] fisierele .xlsx sunt in: {os.path.abspath(TMP)}")
