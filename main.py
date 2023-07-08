from functions import *
def main():
    try:
        print('Selecciona una opcion')
        print('1.Decimal a Binario')
        print('2.Binario a Decimal')
        op = input('Ingrese la opcion: ')
        if op == '1':
            deci = input('Ingrese el número: ')
            if '.' in deci:
                tem = deci.split('.')
                binary = dec_to_bin(int(tem[0]))
                frac_binary = frac_to_bin(tem[1])
                print(f'La parte fraccionaria del número es {binary}.{frac_binary}')
                main()
            elif deci == 'exit':
                print('Fin del programa')
            else:
                binary = dec_to_bin(int(deci))
                print(f'El número en binario es {binary}')
                main()
        elif op == '2':
            binary = input('Ingrese el numero: ')
            temp = bin_to_dec(binary)
            print(f'El numero es: {temp}')
            main()
        else:
            print('Esa no es una opcion valida')
            main()
    except Exception as ex:
        print(ex)
        main()

if __name__ == '__main__':
    main()
