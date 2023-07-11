from functions import *

def main():
    try:
        print('Selecciona una opcion')
        print('1. Decimal a Binario')
        print('2. Binario a Decimal')
        print('3. Decimal a Octal')
        print('4. Octal a Decimal')
        print('5. Hexadecimal a Decimal')
        print('6. Decimal a Hexadecimal')
        print('7. Salir')
        op = input('\nIngrese la opcion: ')

        if op == '1':
            deci = input('Ingrese el número: ')
            binary = dec_to_bin(deci)
            print(f'este es el resultad0 {binary}\n')
            main()

        elif op == '2':
            binary = input('Ingrese el numero: ')
            temp = bin_to_dec(binary)
            print(f'El resultado es: {temp}\n')
            main()
            
        elif op == '3':
            octal = input('Ingrese el numero: ')
            temp = dec_to_oct(octal)
            print(f'El resultado es: {temp}\n')
            main()

        elif op == '4':
            deci = input('Ingrese el numero: ')
            temp = oct_to_dec(deci)
            print(f'El resultado es: {temp}\n')
            main()

        elif op == '5':
            deci = input('Ingrese el numero: ')
            temp = hex_to_dec(deci)
            print(f'El resultado es: {temp}\n')
            main()

        elif op == '6':
            deci = input('Ingrese el numero: ')
            temp = dec_to_hex((deci))
            print(f'El resultado es: {temp}\n')
            main()

        elif op == '7':
            print('\nOyasumi (✿◠‿◠)')

        else:
            print('Esa no es una opcion valida')
            main()

    except Exception as ex:
        print(ex)
        main()


if __name__ == '__main__':
    main()
