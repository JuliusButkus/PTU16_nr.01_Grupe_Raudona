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
        saldytuvas = {str(input("įveskite produktą")): input("Įveskite kiekį") }
    elif tekstas == '3':
        pass
    elif tekstas == '4':
        pass
    elif tekstas == '5':
        pass