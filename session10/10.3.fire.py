# DRUMUL SPRE INDEPENDENTA FINANCIARA (FIRE)  Financial Independence, Retire Early
# =============================================================
# Construim impreuna, pas cu pas, un simulator care raspunde la
# intrebarea:
#   "in cati ani pot trai fara sa mai depind de salariu?"
#
# CONCEPTE FINANCIARE pe care le invatam:
#   - rata de economisire (savings rate)
#   - dobanda compusa (compound interest)
#   - regula 25x / regula 4%:
#       suma de care ai nevoie ca sa "iesi din munca" =
#                       cheltuieli_anuale * 25
#     pentru ca poti retrage 4%/an dintr-un portofoliu
#     diversificat pe viata (studiul Trinity).
#   - puterea timpului: la final, cea mai mare parte din avere
#     vine din randament, NU din ce ai pus tu.
#
# DIN PYTHON folosim TOT ce am invatat (s1-s9):
#   variabile, string-uri si formatare {:,.0f}
#   liste, dictionare, tuple, set
#   if / elif / else, for, while
#
# Cum lucram:
#   - parcurgem cei 4 PASI in ordine
#   - la fiecare TODO oprim si scriem codul impreuna
#   - dupa fiecare pas RULAM ca sa vedem progresul
# =============================================================


# =============================================================
# PASUL 1  —  PROFILUL FINANCIAR
# =============================================================
# CE IMPLEMENTAM:
#   Un DICTIONAR "profil" care strange datele financiare ale unei
#   persoane:
#     - nume                (string)
#     - salariu_net         (int/float)  RON pe luna, dupa taxe
#     - cheltuieli          (int/float)  RON pe luna, TOTAL
#     - patrimoniu_initial  (int/float)  cati bani are deja pusi
#     - randament_anual     (float)      ex: 0.07 = 7%
#                                         (randament tipic ETF
#                                          global pe termen lung)
#
#   Plus:
#     - REPERE          : un TUPLE cu praguri psihologice (100k, 250k...)
#                         si mesajul cand sunt atinse
#     - repere_atinse   : un SET gol, ca sa nu anuntam un reper
#                         de mai multe ori



# TODO 1.1  —  Creeaza dictionarul "profil" cu cele 5 campuri de mai sus.
#
profil = {
    'nume': 'John',
    'salariu_net': 6000,
    'cheltuieli': 5500,
    'patrimoniu_initial': 0,
    'randament_anual': 0.07,
}


# TODO 1.2  —  Creeaza tuple-ul REPERE.
#              Fiecare element este un TUPLE (prag, mesaj).
#              Praguri sugerate: 100_000, 250_000, 500_000, 1_000_000.
#              Mesajele pot fi orice — "primul prag!", "milionar!" etc.
REPERE = (
    (100_000, "primul prag!"),
    (250_000, "primul sfert de milion"),
    (500_000, "jumatatea drumului spre primul milion"),
    (1_000_000, "milionat in RON")
)


# TODO 1.3  —  Creeaza un set gol pentru repere_atinse.
repere_atinse = set()


# =============================================================
# PASUL 2  —  CALCULAM OBIECTIVUL FIRE
# =============================================================
# CE IMPLEMENTAM:
#   Calcule derivate din profil (nu sunt date noi, sunt formule):
#     - cheltuieli_anuale  = cheltuieli lunare * 12
#     - obiectiv_FIRE      = cheltuieli_anuale * 25   (regula 25x)
#     - economii_lunare    = salariu_net - cheltuieli
#     - rata_economisire   = economii_lunare / salariu_net
#     - randament_lunar    = randament_anual / 12
#                            (aproximare lineara, usor de inteles)
#
#   Apoi afisam profilul si obiectivul cu format frumos.
#
# FORMATARE NUMERE:
#   {valoare:,.0f}  ->  inseamna "afiseaza cu separator de mii,
#                       fara zecimale". Ex: 1050000 -> 1,050,000
#   {valoare:>10,.0f}  ->  in plus, aliniere la dreapta pe 10 caractere.
#
# DE CE 25x?
#   Pentru ca retragerea sustenabila e ~4%/an.  1 / 0.04 = 25.


# TODO 2.1  —  Calculeaza cheltuieli_anuale (cheltuieli * 12)
cheltuieli_anuale = profil["cheltuieli"] * 12



# TODO 2.2  —  Calculeaza obiectiv_FIRE (cheltuieli_anuale * 25)
obiectiv_FIRE = cheltuieli_anuale * 25


# TODO 2.3  —  Calculeaza economii_lunare (salariu - cheltuieli)
economii_lunare = profil['salariu_net'] - profil['cheltuieli']


# TODO 2.4  —  Calculeaza rata_economisire (economii_lunare / salariu_net)
#              ATENTIE: feriti-va de impartire la 0 daca profilul e gol!
#              (sau lasati hardcodat 0 cat timp profilul nu e completat)
rata_economisire = economii_lunare / profil['salariu_net']


# TODO 2.5  —  Calculeaza randament_lunar (randament_anual / 12)
randament_lunar = profil['randament_anual'] / 12


# Afisare profil — codul de mai jos foloseste .get() ca sa nu crape
# daca profilul nu e inca completat (puteti il rula de la primul pas).
print(f"=== PROFIL: {profil.get('nume', '?')} ===")
print(f"  salariu net:        {profil.get('salariu_net', 0):>10,.0f} RON/luna")
print(f"  cheltuieli:         {profil.get('cheltuieli', 0):>10,.0f} RON/luna")
print(f"  economii lunare:    {economii_lunare:>10,.0f} RON/luna ({rata_economisire*100:.0f}%)")
print(f"  randament asteptat: {profil.get('randament_anual', 0)*100:.0f}% pe an")
print(f"  patrimoniu start:   {profil.get('patrimoniu_initial', 0):>10,.0f} RON")
print()
print(f"OBIECTIV FIRE:        {obiectiv_FIRE:>10,.0f} RON  (25 x {cheltuieli_anuale:,.0f} chelt/an)")
print()


# =============================================================
# PASUL 3  —  SIMULAREA (WHILE LOOP)
# =============================================================
# CE IMPLEMENTAM:
#   Bucla care simuleaza viata LUNA CU LUNA, pana cand:
#     - patrimoniul atinge sau depaseste obiectivul FIRE,  SAU
#     - depasim 600 de luni (50 ani — safeguard)
#
#   Pentru fiecare luna:
#     1. patrimoniul EXISTENT produce randament:
#          castig_luna = patrimoniu * randament_lunar
#     2. la patrimoniu se adauga castigul + economiile lunii:
#          patrimoniu = patrimoniu + castig_luna + economii_lunare
#     3. tinem doua contoare separate:
#          - contributii_totale  (cati bani am PUS eu)
#          - castig_total        (cati bani au facut banii)
#     4. la fiecare 12 luni: snapshot (afisare + lista pentru raport)
#     5. verificam daca am atins un reper nou (tuple + set)

LUNI_MAX = 600  # 50 de ani

# TODO 3.1  —  Initializeaza variabilele inainte de while:
#   patrimoniu          = profil["patrimoniu_initial"]  (sau .get cu fallback)
#   contributii_totale  = profil["patrimoniu_initial"]
#   castig_total        = 0
#   luna                = 0
#   snapshot_anuali     = []         (lista pentru raport final)
patrimoniu         = profil["patrimoniu_initial"]
contributii_totale = profil["patrimoniu_initial"]
castig_total       = 0
luna               = 0
snapshot_anuali    = []


print("=== SIMULARE LUNA CU LUNA ===")

# TODO 3.2  —  Scrie conditia while:  patrimoniu < obiectiv AND luna < LUNI_MAX

while patrimoniu < obiectiv_FIRE and luna < LUNI_MAX :                       # <-- inlocuieste False cu conditia corecta

    # TODO 3.3  —  incrementeaza luna cu 1
    luna += 1

    # TODO 3.4  —  calculeaza castigul lunii: patrimoniu * randament_lunar
    castig_luna = patrimoniu * randament_lunar

    # TODO 3.5  —  actualizeaza patrimoniu (existent + castig + economii)
    patrimoniu = patrimoniu + castig_luna + economii_lunare

    # TODO 3.6  —  actualizeaza contoarele:
    #   contributii_totale += economii_lunare
    #   castig_total       += castig_luna
    contributii_totale += economii_lunare
    castig_total       += castig_luna

    # TODO 3.7  —  daca luna e multiplu de 12, fa un snapshot anual:
    #   creeaza un dict cu cheile: an, patrimoniu, contributii, castig
    #   adauga-l in snapshot_anuali
    #   afiseaza-l: f"  anul {an:2d} (luna {luna:3d}):  patrimoniu {patrimoniu:>12,.0f} RON"
    if luna % 12 == 0:
        an = luna // 12
        snapshot = {
            'an': an,
            'patrimoniu': patrimoniu,
            'contributii': contributii_totale,
            'castig': castig_total
        }
        snapshot_anuali.append(snapshot)
        print(f"  anul {an:2d} (luna {luna:3d}):  patrimoniu {patrimoniu:>12,.0f} RON")


    # TODO 3.8  —  verifica reperele:
    for prag, mesaj in REPERE:
        if patrimoniu >= prag and prag not in repere_atinse:
          repere_atinse.add(prag)
          print(f"     >>> REPER {prag:,} RON atins: {mesaj}")


# =============================================================
# PASUL 4  —  RAPORTUL FINAL
# =============================================================
# CE IMPLEMENTAM:
#   La iesirea din while:
#     - daca patrimoniu >= obiectiv_FIRE -> FELICITARI, ani + luni
#     - daca rata_economisire <= 0       -> sfat: cheltuielile depasesc venitul
#     - altfel                            -> sfat: creste rata sau randamentul
#
#   Apoi raport "de unde vin banii":
#     - cati au venit din munca       (contributii_totale)
#     - cati au venit din randament   (castig_total)
#     - ce procent reprezinta fiecare
#     - pentru 1 RON pus, cati RON a adaugat piata
#
#   Apoi un mini-grafic ASCII cu snapshot-urile anuale (FOR pe lista).

print()
print("=" * 60)
print("===          RAPORT FINAL          ===")
print("=" * 60)


# TODO 4.1  —  if/elif/else dupa rezultatul simularii:
if patrimoniu >= obiectiv_FIRE:
  ani       = luna // 12
  luni_rest = luna % 12
  print(f"FELICITARI! {profil['nume']} a atins FIRE in {ani} ani si {luni_rest} luni.")
elif rata_economisire <= 0:
  print("ATENTIE: cheltuielile depasesc venitul. FIRE imposibil.")
  print("Sfat: reducerea cheltuielilor e primul pas.")
else:
  print(f"In {LUNI_MAX // 12} ani nu s-a atins FIRE.")
  print("Sfat: creste rata de economisire sau randamentul.")


print()
print(f"  patrimoniu final:        {patrimoniu:>14,.0f} RON")
print(f"  bani pusi de tine:       {contributii_totale:>14,.0f} RON")
print(f"  bani din randament:      {castig_total:>14,.0f} RON")
print()


# TODO 4.2  —  Afiseaza procentul din avere care vine din randament:
if patrimoniu > 0:
  procent_randament = castig_total / patrimoniu * 100
  print(f"  {procent_randament:.0f}% din avere vine din DOBANDA COMPUSA, nu din salariu!")

if contributii_totale > 0:
  multiplicator = castig_total / contributii_totale
  print(f"  Pentru fiecare 1 RON economisit, piata a adaugat {multiplicator:.2f} RON.")
pass


# TODO 4.3  —  Afiseaza mini-grafic ASCII al evolutiei (FOR pe snapshot_anuali):
print("--- evolutie an cu an ---")
for snap in snapshot_anuali:
  bar_len = int(snap["patrimoniu"] / obiectiv_FIRE * 40)
  bar = "#" * bar_len
  print(f"  an {snap['an']:2d}:  {snap['patrimoniu']:>11,.0f}  |{bar}")


# =============================================================
# DUPA CE AM TERMINAT  —  EXTINDERI (provocari bonus)
# =============================================================
# 1. Schimba profilul cu DATELE TALE reale si reruleaza.
# 2. Modifica rata de economisire de la 30% la 50% si compara
#    cu cati ani diferenta ajungi la FIRE.
# 3. Adauga inflatie: cheltuielile cresc 3% pe an  ->  obiectivul
#    se MISCA pe parcurs. Trebuie recalculat in fiecare an.
# 4. Adauga o majorare salariala automata la fiecare 24 luni (+5%).
# 5. Calculeaza "Coast FIRE": cati bani trebuie sa ai ACUM ca,
#    fara sa mai pui nimic, sa ajungi singur la FIRE pana la
#    varsta de 60 de ani.
# =============================================================