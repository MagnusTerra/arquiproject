from functions import *
def main():
    try:
        print('Selecciona una opcion')
        print('1. Decimal a Binario')
        print('2. Binario a Decimal')
        print('3. Sumar numeros binarios')
        op = input('Ingrese la opcion: ')
        if op == '1':
            deci = input('Ingrese el número: ')
            if '.' in deci:
                tem = deci.split('.')
                binary = dec_to_bin(int(tem[0]))
                frac_binary = frac_to_bin(tem[1])
                print(f'La parte fraccionaria del número es {binary}.{frac_binary}\n')
                main()
            elif deci == 'exit':
                print('Fin del programa')
            else:
                binary = dec_to_bin(int(deci))
                print(f'El número en binario es {binary}')
                main()
        elif op == '2':
            binary = input('Ingrese el numero: ')
            numeros = ['2', '3', '4', '5', '6', '7', '8','9']
            if any(numero in binary for numero in numeros):
                print("Ese no un numero binario \n ")
                main()
            else:
                temp = bin_to_dec(binary)
                print(f'El numero es: {temp}\n')
                main()
            
        else:
            print('Esa no es una opcion valida')
            main()
    except Exception as ex:
        print(ex)
        main()

if __name__ == '__main__':
    main()
