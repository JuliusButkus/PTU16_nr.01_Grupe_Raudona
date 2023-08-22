import time

def intro(intro_saldytuwas, delay=0.05):
    for raidės in intro_saldytuwas:
        print(raidės, end='', flush=True)
        time.sleep(delay)
intro(f"Išmanusis Daugiafunkcinis\033[91m TSR Liaudies Šaldytuwas ZVEZDA 16 \u262d")
meniukas = '''
1. Meniu
2. Patiekalai
\033[92m
3. Ką norite įdėti?
4. Ką norite išimti?
5. Ką norite pasigaminti?
6. Ką reikia išpilti(nuleisti(išmesti))?
0. Uždaryti Šaldytuwą?
\033[97m
'''
#print(meniukas)

saldytuvas = {}

print(meniukas)
def operacijos_parinktis():
    tekstas = input('Pasirinkite operacija: ')   
    if tekstas == '0':
        return 0
    elif tekstas == '1':
        produktas = input("Pridekite produkta: ")
        produkto_kiekis = int(input("Pridekite produkto kieki: "))
        saldytuvas[produktas] = produkto_kiekis
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
operacijos_parinktis()
