def dec_to_bin(num):
    # Divide el número en parte entera y parte decimal, y asigna un valor predeterminado de '0' si no hay parte decimal
    int_part, frac_part = (num.split('.') + ['0'])[:2]
    
    # Convierte la parte entera en un valor absoluto para asegurarse de que sea positiva
    int_part = abs(int(int_part))
    
    # Convierte la parte decimal en un número de punto flotante
    frac_part = float('0.' + frac_part)

    # Convierte la parte entera en binario
    int_result = ''
    while int_part > 0:
        int_result = str(int_part % 2) + int_result
        int_part //= 2

    # Convierte la parte decimal en binario
    frac_result = ''
    while frac_part > 0 and len(frac_result) < 7:
        frac_part *= 2
        if frac_part >= 1:
            frac_result += '1'
            frac_part -= 1
        else:
            frac_result += '0'

    # Combina la parte entera y la parte decimal binarias para obtener el resultado final y si la no hay parte decimal solo devuelve la entera
    result = int_result + '.' + frac_result if frac_result else int_result
    
    # Agrega el signo negativo al resultado si el número original es negativo
    if num.startswith('-'):
        result = '-' + result

    return result

def bin_to_dec(num):
    numeros = ['2', '3', '4', '5', '6', '7', '8','9']
    if any(numero in num for numero in numeros):
            result = 'Este no es un numero binario'
    
    else:
        
        init_part, frac_part = (num.split('.') + ['0'])[:2]  # Divide el número en parte entera y parte decimal
        
        cont = 0  # Variable para almacenar la parte entera convertida a decimal
        positive_raised = 0  # Exponente positivo de la base 2
        upside_text1 = init_part[::-1]  # Invierte el orden de los dígitos de la parte entera

        # Convierte la parte entera del número binario en su representación decimal
        for i in upside_text1:
            i = int(i)
            cont += i * (2**positive_raised)  # Multiplica cada dígito por la potencia correspondiente de 2
            positive_raised += 1

        upside_text2 = frac_part[::-1]  # Invierte el orden de los dígitos de la parte decimal
        cont2 = 0  # Variable para almacenar la parte decimal convertida a decimal
        negative_raised = -1  # Exponente negativo de la base 2

        # Convierte la parte decimal del número binario en su representación decimal
        for j in upside_text2:
            j = int(j)
            cont2 += j * (2** negative_raised)  # Multiplica cada dígito por la potencia correspondiente de 2, pero con exponentes negativos
            negative_raised -= 1

        result = f'{cont + cont2}' if cont2 else cont  # Combina la parte entera y decimal en el resultado final

    return result



#OPERACIONES BASICAS CON BINARIOS
def sum_bin(num1, num2):
    num1 = int(bin_to_dec(num1))
    num2 = int(bin_to_dec(num2))
    resultado = num1 + num2
    print(f'La suma de {dec_to_bin(str(num1))} y {dec_to_bin(str(num2))} es igual a: {dec_to_bin(str(resultado))}\n')

def sub_bin(num1, num2):
    num1 = int(bin_to_dec(num1))
    num2 = int(bin_to_dec(num2))
    resultado = num1 - num2
    print(f'La resta de {dec_to_bin(str(num1))} y {dec_to_bin(str(num2))} es igual a: {dec_to_bin(str(resultado))}\n')

def mul_bin(num1, num2):
    num1 = int(bin_to_dec(num1))
    num2 = int(bin_to_dec(num2))
    resultado = num1 * num2
    print(f'La multiplicacin de {dec_to_bin(str(num1))} y {dec_to_bin(str(num2))} es igual a: {dec_to_bin(str(resultado))}\n')


