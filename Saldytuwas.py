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

def prideti_produkta(saldytuvas):
    pavadinimas = input("Iveskite produkto pavadinima: ")
    kiekis = float(input("Iveskite produkto kieki: "))
    saldytuvas[pavadinimas] += kiekis
    print(saldytuvas)

def funkcija_02():
    pass

def funkcija_03():
    pass

def funkcija_04():
    pass

def funkcija_05():
    pass

def funkcija_06():
    pass

while True:
    print(meniukas)
    tekstas = input('Pasirinkite operacija: ')
    
    if tekstas == '0':
        break
    elif tekstas == '1':
        print(prideti_produkta(saldytuvas))
    elif tekstas == '2':
        keisti_produkta = input("pasirinkite produkta: ")
        prideti_kieki = int(input("pasirinkite kieki: "))
        if keisti_produkta in saldytuvas:
            saldytuvas[produktas] += prideti_kieki
            print(f'{saldytuvas[keisti_produkta]}')
    elif tekstas == '3':
        produktas = input("Iveskite koki produkta norite pasalinti: ")
        kiekis = int(input('Iveskite koki kieki produkto norite pasalinti: '))
        
        if produktas in saldytuvas:
            saldytuvas[produktas] -= kiekis
            if saldytuvas[produktas] <= 0:
                print(f'Nepakankamas {produktas} kiekis')
            else:
                print(f'{produktas} saldytuve yra: {saldytuvas[produktas]}')
    elif tekstas == '4':
        produktu_perziura = saldytuvas.items()
        print(f'"Šaldytuve yra šių produktų: {saldytuvas}"')
        print(f'Kūnas šaukia, trūksta Vita-mi-NŲŲ!')
    elif tekstas == '5':
        paieska = input("Įveskite norima rasti produkta: ")
        if paieska in saldytuvas:
            print(paieska, saldytuvas[paieska])
        else:
            print(" Tokio produkto šaldytuve nėra ")
