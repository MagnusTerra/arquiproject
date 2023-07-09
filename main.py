from functions import *

def main():
    try:
        print('Selecciona una opcion')
        print('1.Decimal a Binario')
        print('2.Binario a Decimal')
        print('3.Salir')
        op = input('Ingrese la opcion: ')

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
            print('Saliendo del programa') 

        else:
            print('Esa no es una opcion valida')
            main()

    except Exception as ex:
        print(ex)
        main()


if __name__ == '__main__':
    main()
