import time
#from IPython.display import clear_output

class Saldytuvas:

    saldytuvas = {
        'Lašiniai': 10,
        'Sviestas': 5,
        'Pienas': 5.0, 
        'Rūgpienis': 4.3,
        'Grietinė': 11.3,
        'Daktariška Dešra': 0.8,
        'Bulvės': 10,
        'Burokėliai': 35,
        'Žigulinis Alus': 5.5,
        'Degtinė': 3.5,
        'Dujokaukė': 1
    }
    receptukai = {
        'Kiaušinienė':{  
            'Kiaušiniai': 2,
            'Pienas': 0.5,
            'Dešra':1},
        'Salotos':{
            'Agurkai': 2,
            'Pomidorai': 2,
            'Grietinė': 0.5,
            'Svogūnai': 1,
            'Lašiniai': 1.5},
        'Plombyras':{
            'Pienas': 1,
            'Cukrus': 0.5,
            'Grietinė': 1,
            'Sviestas': 0.5},
        'Barščiai':{
            'Burokėliai': 3,
            'Grietinė': 0.2,
            'Žigulinis Alus': 0.5,
            'Dešra': 0.1,
            'Lašiniai': 2,
            'Bulvės': 4},
        'Кончининская':{
            'Žigulinis Alus': 0.15,
            'Degtinė': 0.3,
            'Agurkai': 0.5}    
    }


    def prideti_produkta(self):
        produktas = input("Iveskite produkto pavadinima: ")
        kiekis = float(input("Iveskite produkto kieki: "))
        self.saldytuvas[produktas] = kiekis
        print(f"{produktas}: {self.saldytuvas[produktas]}")

    def papildyti(self):
        produktas = input("pasirinkite produkta: ")
        kiekis = float(input("pasirinkite kieki: "))
        if produktas in self.saldytuvas:
            self.saldytuvas[produktas] += kiekis
            print(f'{self.saldytuvas[produktas]}')
        else:
            self.saldytuvas[produktas] == kiekis
            print(f'{self.saldytuvas[produktas]}')

    def isumti_kieki(self, produktas):
        pass #daro Lukas

    def turinys(self, produktas):
        pass # Daro Vytautas

    def isskoti_produkto(self, produktas):
        pass #Dainius

    def receptas(self,):
        pass #kas pirmesnis tas gudresnis (prasinesti jeigu padare)


def intro(intro_saldytuwas, delay=0.001):
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


'''
def saldytuvo_aprasas(saldytuwo_aprasas, delay=0.08):
    for raidės in saldytuwo_aprasas:
        print(raidės, end='', flush=True)
        time.sleep(delay)
#saldytuvo_aprasas(f"\n\033[92m APRAŠAS \n{sald_apras}")
saldytuvo_aprasas([print(key,':',value) for key, value in sald_apras.items()])
'''
#def prideti_produkta(saldytuvas):
    #pavadinimas = input("Iveskite produkto pavadinima: ")
    #kiekis = float(input("Iveskite produkto kieki: "))
    #saldytuvas[pavadinimas] = kiekis
    # print(f"{saldytuvas[pavadinimas]}")
#     return saldytuvas

# def produkto_papildymas(saldytuvas):
#     pavadinimas = input("pasirinkite produkta: ")
#     prideti_kieki = float(input("pasirinkite kieki: "))
#     if pavadinimas in saldytuvas:
#         saldytuvas[pavadinimas] += prideti_kieki
#         print(f'{saldytuvas[pavadinimas]}')
#     return saldytuvas

# def produkto_isemimas(saldytuvas):
#     produktas = input("Įveskite Produktą, kurį Norite Pašalinti: ")
#     kiekis = float(input('Įveskite Produkto Kiekį, Kurį Norite Pašalinti: '))
#     if produktas in saldytuvas:
#         saldytuvas[produktas] -= kiekis
#         if saldytuvas[produktas] <= 0:
#             del saldytuvas[produktas]
#             print(f'Pašalinta(s) {produktas}')
#         else:
#             print(f'{produktas} Šaldytuve yra: {saldytuvas[produktas]}')
#     return saldytuvas

# def produkto_ispilimas(saldytuvas):
#     produktas = input("Įveskite Produktą, Kurį Norite Išpilti: ")
#     kiekis = float(input('Įveskite Produkto Kiekį Išpilčiai: '))
#     if produktas in saldytuvas:
#         saldytuvas[produktas] -= kiekis
#         if saldytuvas[produktas] <= 0:
#             del saldytuvas[produktas]
#             print(f'Išpiltas {produktas}')
#             time.sleep(2)
#             print(f'Nu jo.. Žodžiu.')
#         else:
#             time.sleep(1.5)
#             print(f'{produktas} Šaldytuve Yra: {saldytuvas[produktas]}')
#     return saldytuvas

# def produktu_turinys():
#     print(f'\033[92m1. Šaldytuvo Turinys: ')
#     for key, value in saldytuvas.items():
#         print(key,':',value) 
#     #produktu_perziura = saldytuvas.items()
#     #print(f'"Šaldytuve Yra Šių Produktų: {saldytuvas}"')

# def ieskoti_produkto(saldytuvas):
#     paieska = input("Įveskite Norimą Rasti Produktą: ")
#     if paieska in saldytuvas:
#         print(paieska, saldytuvas[paieska])
#     else:
#         print(" Tokio Produkto Šaldytuve Nėra ! ")

# def receptas(saldytuvas, receptukai):
#     print(f"\033[92m„Gastro Patirtys“: ")
#     time.sleep(0.5)
#     print(f'\n\033[92m{receptukai}')
#     pasirinktas_receptas = input("Pasirinkte „Gastro“ Receptą: ")
#     if pasirinktas_receptas in receptukai:
#         rasti_produktai = {}
#         for produktas, kiekis in receptukai[pasirinktas_receptas].items():
#             if produktas in saldytuvas:
#                 rasti_produktai[produktas] = saldytuvas[produktas] - kiekis
#             else:
#                 rasti_produktai[produktas] = -kiekis
#         for produktas, kiekis in rasti_produktai.items():
#             if kiekis >= 0:
#                 print(f'{produktas} užtenka')
#             else:
#                 print(f'{produktas} neužtenka {abs(kiekis)}')
#     return pasirinktas_receptas
saldytuvas = Saldytuvas()
while True:
    #print(meniukas)
    # pasimti duomenis is JSON failo
    # with open("saldytuvas.json", "w") as saldytuvo_failas:
    #     saldytuvo_failas.dump(saldytuvas, saldytuvo_failas, indent=2, ensure_ascii=False)
    tekstas = input('Išsirinkite Parinktį!: ')
    
    if tekstas == '0':
        print(f"\033[92m>>>>>>>Я ОТКЛЮЧАЮСЬ!<<<<<<<<")
        time.sleep(4)
        print(f"\n\033[91m>Ištrauk Lizdą Kitakart Veikiau Jau!")
        time.sleep(0.85)
        #istrinimas = clear_output(wait=False)
        # irasyti duomenis i JSON faila
        # json_saldyvas = json.dumps(saldytuvas, indent=2, ensure_ascii=False)
        # print(json_saldyvas)
        break
    elif tekstas == '1':
        print(produktu_turinys())
    elif tekstas == '2':
        print(ieskoti_produkto(saldytuvas))
    elif tekstas == '3':
        saldytuvas.prideti_produkta()
    elif tekstas == '4':        
        saldytuvas = produkto_isemimas(saldytuvas)
    elif tekstas == '5':
        saldytuvas.papildyti()
    elif tekstas == '6':
        print(receptas(saldytuvas, receptukai))
    elif tekstas == '7':
        saldytuvas = produkto_ispilimas(saldytuvas)    
    elif tekstas == '8':
        #print(saldytuvo_aprasas(saldytuwo_aprasas, delay=0.08)) Neveikia kažkodie
        pass
    elif tekstas != ['1','2', '3','4','5','6','7','8']:
        print(f'Šaldytuve Nėra Tokios Parinkties!')
