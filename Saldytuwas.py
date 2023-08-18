#ŠALDYTUVAS
'''
1 - pridėti naują produktą
2 - papildyti produkto kiekį
3 - ištraukti produktą nurodant kiekį
4 - peržiūrėti produktus
5 - ieškoti produktų
0 - išėjimas
'''
saldytuvas = {}

while True:
    tekstas = input('Pasirinkite operacija: ')
    if tekstas == '0':
        break
    elif tekstas == '1':
        pass
    elif tekstas == '2':
        pass
    elif tekstas == '3':
        pass
    elif tekstas == '4':
        produktu_perziura = saldytuvas.items()
        print(f'"Šaldytuve yra šių produktų: {saldytuvas}"')
        print(f'Kūnas šaukia, trūksta Vita-mi-NŲŲ!')
    elif tekstas == '5':
        pass
