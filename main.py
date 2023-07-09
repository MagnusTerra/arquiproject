from functions import *

def main():
    try:
        print('Selecciona una opcion')
        print('1. Decimal a Binario')
        print('2. Binario a Decimal')
        print('3. Sumar numeros binarios')
        print('4. Restar numeros binarios')
        print('5. Multiplicar numeros binarios')
        print('7. Salir')
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
            num1 = input('\nIngrese el primer numero: ')
            num2 = input('Ingrese el segundo numero: ')
            sum_bin(num1, num2)
            main()
        
        elif op == '4':
            num1 = input('\nIngrese el primer numero: ')
            num2 = input('Ingrese el segundo numero: ')
            sub_bin(num1, num2)
            main()
        
        elif op == '5':
            num1 = input('\nIngrese el primer numero: ')
            num2 = input('Ingrese el segundo numero: ')
            mul_bin(num1, num2)
            main()
        
        else:
            print('Esa no es una opcion valida')
            main()

    except Exception as ex:
        print(ex)
        main()


if __name__ == '__main__':
    main()
