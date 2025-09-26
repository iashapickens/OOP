import CellphoneClass as c

def main():
    man = input('Enter the manufacturer: ')
    mod = input('Enter the model number: ')
    retail = float(input('Enter the retail price: '))

    phone = c.CellPhone(man, mod, retail)

    print('Here is the data that you entered:')
    print('Manufacturer:', phone.get_manufact())
    print('Model Number:', phone.get_model())
    print(f'Retail Price: ${phone.get_retail_price():,.2f}')

main()
