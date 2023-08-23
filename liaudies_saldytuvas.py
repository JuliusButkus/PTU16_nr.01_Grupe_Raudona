import time
#from IPython.display import clear_output

def intro(intro_saldytuwas, delay=0.03):
    for raidės in intro_saldytuwas:
        print(raidės, end='', flush=True)
        time.sleep(delay)
intro(f"Išmanusis Daugiafunkcinis\033[91m \u262d LTSR Liaudies Šaldytuvas SNAIGĖ-317")

time.sleep(0.5)
intro(f"\n\033[92m ZAGRUSHKA SYSTEMU...")

time.sleep(2)
print(f'\n\033[95mSveiki!')
time.sleep(1)
meniukas = '''
| 1. Turinys                              |
| 2. Paieška                              |
\033[92m                                  
| 3. Ką norite įdėti?                     |  
| 4. Ką norite išimti?                    |
| 5. Ką norite papildyti?                 |
| 6. „Gastro Patirtys“                    |  
| 7. Ką reikia išpilti?                   |
| 8. Apie Šaldytuvą                       |
| 0. Išjungti Šaldytuvą?                  |
\033[97m
'''
time.sleep(1.5)
intro(f"\n\033[92mPARINKTYS")
print(meniukas)

sald_apras = {
    'SNAIGĖ-317': {
        'Gamybos data': '1984',
        'Eksplotuotojas': 'Омски Газ Мяс(ОГМ)',
        'Pagaminta': 'Vilniuje: Tautų Draugystės Ordino Elektromechanikos Kombinatas „Litva“',
        'Spalva': 'Pilkšva',
        'Galia': '2.8 kW',
        'Svoris': '1860 kg',
        'Triukšmo lygis': '67 dB',
        'Ar Spyna Yra?': 'Taip, Nes Viskas Išbildėtų',
        'Pagaminta iš': 'Švino; Volframo; Grafito; Bakelito etc...',
        'Termobranduolinė apsauga?': 'Yra, Nes nu Liaudies Priešai-Kapitalistai Užbombins.. Nu.',
    }
}
intro(f'\n\033[92m{sald_apras}')
#intro([print(key,':',value) for key, value in sald_apras.items()])

saldytuvas = {
    '1. Lašiniai': {
        'Kiekis': 10,
    },
    '2. Sviestas': {
        'Kiekis': 5,
    },
    '3. Pienas': {
        'Kiekis': 5.0,
        'Būsena': 'Šviežias',
    },
    '4. Rūgpienis': {
        'Kiekis': 4.3,
        'Būsena': 'Supelijęs',
    },
    '5. Grietinė': {
        'Kiekis': 11.3,
    },
    '6. Daktariška Dešra': {
        'Kiekis': 0.8,
        'Būsena': 'Dar Gera, Tarkim',
    },
    '7. Bulvės': {
        'Kiekis': 10,
        'Būsena': 'Nuskustos',
    },
    '8. Burokėliai': {
        'Kiekis': 35,
    },
    '9. Žigulinis Alus': {
        'Kiekis': 5.5,
    },
    '10. Degtinė': {
        'Kiekis': 3.5,
    },
    '11. Dujokaukė': {
        'Kiekis': 1,
        'Modelis': 'GP-5',
        'Būsena': 'Paruošta; Su Abestiniu Filtru',
    }
}

receptukai = {
    '1. Kiaušinienė':{  
        'Kiaušiniai': 2,
        'Pienas': 0.5,
        'Dešra':1},
    '2. Salotos':{
        'Agurkai': 2,
        'Pomidorai': 2,
        'Grietinė': 0.5,
        'Svogūnai': 1,
        'Lašiniai': 1.5},
    '3. Plombyras':{
        'Pienas': 1,
        'Cukrus': 0.5,
        'Grietinė': 1,
        'Sviestas': 0.5},
    '4. Barščiai':{
        'Burokėliai': 3,
        'Grietinė': 0.2,
        'Žigulinis Alus': 0.5,
        'Dešra': 0.1,
        'Lašiniai': 2,
        'Bulvės': 4},
    '5. Кончининская':{
        'Žigulinis Alus': 0.15,
        'Degtinė': 0.3,
        'Agurkai': 0.5}    
}
'''
def saldytuvo_aprasas(saldytuwo_aprasas, delay=0.08):
    for raidės in saldytuwo_aprasas:
        print(raidės, end='', flush=True)
        time.sleep(delay)
#saldytuvo_aprasas(f"\n\033[92m APRAŠAS \n{sald_apras}")
saldytuvo_aprasas([print(key,':',value) for key, value in sald_apras.items()])
'''

def prideti_produkta(saldytuvas):
    pavadinimas = input("Iveskite produkto pavadinima: ")
    kiekis = float(input("Iveskite produkto kieki: "))
    saldytuvas[pavadinimas] = kiekis
    print(f"{saldytuvas[pavadinimas]}")

def produkto_papildymas(saldytuvas):
    pavadinimas = input("pasirinkite produkta: ")
    prideti_kieki = float(input("pasirinkite kieki: "))
    if pavadinimas in saldytuvas:
        saldytuvas[pavadinimas] += prideti_kieki
        print(f'{saldytuvas[pavadinimas]}')

def produkto_isemimas(saldytuvas):
    produktas = input("Įveskite Produktą, kurį Norite Pašalinti: ")
    kiekis = float(input('Įveskite Produkto Kiekį, Kurį Norite Pašalinti: '))
    if produktas in saldytuvas:
            saldytuvas[produktas] -= kiekis
            if saldytuvas[produktas] <= 0:
                del saldytuvas[produktas]
                print(f'Pašalinta(s) {produktas}')
            else:
                print(f'{produktas} Šaldytuve yra: {saldytuvas[produktas]}')
def produkto_ispilimas(saldytuvas):
    produktas = input("Įveskite Produktą, Kurį Norite Išpilti: ")
    kiekis = float(input('Įveskite Produkto Kiekį Išpilčiai: '))
    if produktas in saldytuvas:
            saldytuvas[produktas] -= kiekis
            if saldytuvas[produktas] <= 0:
                del saldytuvas[produktas]
                print(f'Išpiltas {produktas}')
                time.sleep(2)
                print(f'Nu jo.. Žodžiu.')
            else:
                time.sleep(1.5)
                print(f'{produktas} Šaldytuve Yra: {saldytuvas[produktas]}')

def produktu_turinys():
    print(f'\033[92m1. Šaldytuvo Turinys: ')
    [print(key,':',value) for key, value in saldytuvas.items()]
    #produktu_perziura = saldytuvas.items()
    #print(f'"Šaldytuve Yra Šių Produktų: {saldytuvas}"')

def ieskoti_produkto(saldytuvas):
    paieska = input("Įveskite Norimą Rasti Produktą: ")
    if paieska in saldytuvas:
        print(paieska, saldytuvas[paieska])
    else:
        print(" Tokio Produkto Šaldytuve Nėra ! ")

def receptas(saldytuvas, receptukai):
    print(f"\033[92m„Gastro Patirtys“: ")
    time.sleep(0.5)
    print(f'\n\033[92m{receptukai}')
    pasirinktas_receptas = input("Pasirinkte „Gastro“ Receptą: ")
    if pasirinktas_receptas in receptukai:
        rasti_produktai = {}
        for produktas, kiekis in receptukai[pasirinktas_receptas].items():
            if produktas in saldytuvas:
                rasti_produktai[produktas] = saldytuvas[produktas] - kiekis
            else:
                rasti_produktai[produktas] = -kiekis
        for produktas, kiekis in rasti_produktai.items():
            if kiekis >= 0:
                print(f'{produktas} užtenka')
            else:
                print(f'{produktas} neužtenka {abs(kiekis)}')

while True:
    #print(meniukas)
    tekstas = input('Išsirinkite Parinktį!: ')
    
    if tekstas == '0':
        print(f"\033[92m>>>>>>>Я ОТКЛЮЧАЮСЬ!<<<<<<<<")
        time.sleep(4)
        print(f"\n\033[91m>Ištrauk Lizdą Kitakart Veikiau Jau!")
        time.sleep(0.85)
        #istrinimas = clear_output(wait=False)
        break
    elif tekstas == '3':
        print(prideti_produkta(saldytuvas))
    elif tekstas == '5':
        print(produkto_papildymas(saldytuvas))
    elif tekstas == '4':        
        produkto_isemimas(saldytuvas)
    elif tekstas == '1':
        produktu_turinys()
    elif tekstas == '6':
        print(receptas(saldytuvas, receptukai))
    elif tekstas == '2':
        print(ieskoti_produkto(saldytuvas))
    elif tekstas == '7':
        print(produkto_ispilimas(saldytuvas))    
    elif tekstas == '8':
        #print(saldytuvo_aprasas(saldytuwo_aprasas, delay=0.08)) Neveikia kažkodie
        pass
    elif tekstas >= '9':
        print(f'Šaldytuve Nėra Tokios Parinkties!')
