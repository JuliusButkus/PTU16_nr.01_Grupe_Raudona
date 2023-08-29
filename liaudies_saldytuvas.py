import time
import json
#from IPython.display import clear_output

try:
    with open("liaudies_maistas.json", "r+", encoding="utf-8") as saldytuvas_dict:
        saldytuvas = json.load(saldytuvas_dict)
except:
    saldytuvas = {}
    with open("liaudies_maistas.json", "w", encoding="utf-8") as saldytuvas_dict:
        json.dump(saldytuvas, saldytuvas_dict)

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

    def isimti_kieki(self): 
        produktas = input("Įveskite Produktą, kurį Norite Pašalinti: ")
        kiekis =float(input('Įveskite Produkto Kiekį, Kurį Norite Pašalinti: '))
        if produktas in self.saldytuvas:
            if self.saldytuvas[produktas] >= kiekis:
                self.saldytuvas[produktas] -= kiekis
                if self.saldytuvas[produktas] <= 0:
                    del self.saldytuvas[produktas]
                    print(f'Pašalinta(s) {produktas}')
                else:
                    print(f'{produktas} Šaldytuve yra: {self.saldytuvas[produktas]}')
            else:
                print(f"Neuztenka {produktas} saldytuve")
        else:
            print(f"{produktas} nera saldytuve")
        return self.saldytuvas

    def turinys(self):
        print(f'\033[92m1. Šaldytuvo Turinys: ')
        for key, value in self.saldytuvas.items():
            print(key,':',value) 
        return self.saldytuvas
    
    def ieskoti_produkto(self):
        produktas = input("Iveskite kokio produkto ieškote? ")
        if produktas in self.saldytuvas:
            kiekis = self.saldytuvas[produktas]
            print(f"Produktas: {produktas} šaldytuve yra, kiekis: {kiekis}")
        else:
            print("Tokio produkto šaldytuve nėra")
    

class Receptų_knyga(Saldytuvas):
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
    def produktas(self):
        print("veikia")

    def receptukas(self):
        print(f"\033[92m„Gastro Patirtys“: ")
        time.sleep(0.001)
        print(f'\n\033[92m{self.receptukai}')
        pasirinktas_receptas = input("Pasirinkte „Gastro“ Receptą: ")
        if pasirinktas_receptas in self.receptukai:
            rasti_produktai = {}
            for produktas, kiekis in self.receptukai[pasirinktas_receptas].items():
                if produktas in self.saldytuvas:
                    rasti_produktai[produktas] = self.saldytuvas[produktas] - kiekis
                else:
                    rasti_produktai[produktas] = -kiekis
            for produktas, kiekis in rasti_produktai.items():
                if kiekis >= 0:
                    print(f'{produktas} užtenka')
                else:
                    print(f'{produktas} neužtenka {abs(kiekis)}')
        #return pasirinktas_receptas

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
        'Talpa': '1024L; Vieno Gigalitro',
        'Triukšmo lygis': '67 dB',
        'Ar Spyna Yra?': 'Taip, Nes Viskas Išbildėtų',
        'Pagaminta iš': 'Švino; Volframo; Grafito; Bakelito etc...',
        'Termobranduolinė apsauga?': 'Yra, Nes nu Liaudies Priešai-Kapitalistai Užbombins.. Nu.',
    }
}
intro(f'\n\033[92m{sald_apras}')
#intro([print(key,':',value) for key, value in sald_apras.items()])

saldytuvas = Saldytuvas()
receptas = Receptų_knyga()
while True:
    tekstas = input(f"\n\033 Išsirinkite Parinktį!: ")
    if tekstas == '0':
        print(f"\033[92m>>>>>>>Я ОТКЛЮЧАЮСЬ!<<<<<<<<")
        time.sleep(4)
        print(f"\n\033[91m>Ištrauk Lizdą Kitakart Veikiau Jau!")
        time.sleep(0.85)
        with open("liaudies_maistas.json", "w", encoding="utf-8") as saldytuvas_dict:
            saldytuvas_dict = json.dump(saldytuvas.turinys(), saldytuvas_dict, indent=2)
        break
    elif tekstas == '1':
        saldytuvas.turinys()
    elif tekstas == '2':
        saldytuvas.ieskoti_produkto()
    elif tekstas == '3':
        saldytuvas.prideti_produkta()
    elif tekstas == '4':        
        saldytuvas.isimti_kieki()
    elif tekstas == '5':
        saldytuvas.papildyti()
    elif tekstas == '6':
        receptas.receptukas()     
    elif tekstas != ['1','2', '3','4','5','6']:
        print(f'Šaldytuve Nėra Tokios Parinkties!')
