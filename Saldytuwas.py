#FUNKCINIS ŠALDYTUVAS
meniukas = '''
1 - pridėti naują produktą
2 - papildyti produkto kiekį
3 - ištraukti produktą nurodant kiekį
4 - peržiūrėti produktus
5 - ieškoti produktų
0 - išėjimas
'''
saldytuvas = {}
receptukai = {
    'Kiausiniene':{  
        'Kiausinis': 2,
        'Pienas': 0.5,
        'Desra':1},
    'Salotos':{
        'Agurkas': 2,
        'Pomidorai': 2,
        'Grietine': 0.5}
          }

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
    produktas = input("Iveskite koki produkta norite pasalinti: ")
    kiekis = float(input('Iveskite koki kieki produkto norite pasalinti: '))
    if produktas in saldytuvas:
            saldytuvas[produktas] -= kiekis
            if saldytuvas[produktas] <= 0:
                del saldytuvas[produktas]
                print(f'Pasalintas {produktas}')
            else:
                print(f'{produktas} saldytuve yra: {saldytuvas[produktas]}')

def funkcija_04():
    pass

def ieskoti_produkto(saldytuvas):
    paieska = input("Įveskite norima rasti produkta: ")
    if paieska in saldytuvas:
        print(paieska, saldytuvas[paieska])
    else:
        print(" Tokio produkto šaldytuve nėra ")

def receptas(saldytuvas, receptukai):
    pasirinktas_receptas = input("pasirinkte receptas")
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
    print(meniukas)
    tekstas = input('Pasirinkite operacija: ')
    
    if tekstas == '0':
        break
    elif tekstas == '1':
        print(prideti_produkta(saldytuvas))
    elif tekstas == '2':
        print(produkto_papildymas(saldytuvas))
    elif tekstas == '3':        
        produkto_isemimas(saldytuvas)
    elif tekstas == '4':
        produktu_perziura = saldytuvas.items()
        print(f'"Šaldytuve yra šių produktų: {saldytuvas}"')
        print(f'Kūnas šaukia, trūksta Vita-mi-NŲŲ!')
    elif tekstas == '5':
        print(ieskoti_produkto(saldytuvas))
    elif tekstas == '6':
        print(receptas(saldytuvas, receptukai))
    
    
