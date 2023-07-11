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

            if negative_raised < -6:
                break
        
        result = f'{cont + cont2}' if cont2 else cont  # Combina la parte entera y decimal en el resultado final
    
    return result


def dec_to_oct(num):
    try:
        # Divide el número en parte entera y parte decimal, y asigna un valor predeterminado de '0' si no hay parte decimal
        int_part, frac_part = (num.split('.') + ['0'])[:2]

        # Convierte la parte entera en un valor absoluto para asegurarse de que sea positiva
        int_part = abs(int(int_part))

        # Convierte la parte decimal en un número de punto flotante
        frac_part = float('0.' + frac_part)

        # Convierte la parte entera en octal
        int_result = ''
        while int_part > 0:
            int_result = str(int_part % 8) + int_result
            int_part //= 8

        frac_octal_result = ''
        # Convierte la parte decimal en octal
        while frac_part != 0 and len(frac_octal_result) < 7:
            frac_part *= 8  # Multiplica la parte decimal por 8
            digito_octal = int(frac_part)  # Obtiene el dígito octal actual
            frac_octal_result += str(digito_octal)  # Agrega el dígito octal a la cadena resultante
            frac_part -= digito_octal  # Resta el dígito octal de la parte decimal

        # Combina la parte entera y la parte decimal octal para obtener el resultado final y si no hay parte decimal solo devuelve la entera
        result = int_result + '.' + frac_octal_result if frac_octal_result else str(int_result)

        # Agrega el signo negativo al resultado si el número original es negativo
        if num.startswith('-'):
            result = '-' + result

        return result
    except ValueError:
        return 'Error: El valor ingresado no es un número decimal valido.'

def oct_to_dec(num):
    try:
        numeros = ['8','9']
        if any(numero in num for numero in numeros):
            result = 'Este no es un número octal'
        else:
            int_part, frac_part = (num.split('.') + ['0'])[:2]  # Divide el número en parte entera y parte decimal

            cont = 0  # Variable para almacenar la parte entera convertida a decimal
            positive_raised = 0  # Exponente positivo de la base 8
            upside_text1 = int_part[::-1]  # Invierte el orden de los dígitos de la parte entera

            # Convierte la parte entera del número octal en su representación decimal
            for i in upside_text1:
                i = int(i)
                cont += i * (8**positive_raised)  # Multiplica cada dígito por la potencia correspondiente de 8
                positive_raised += 1

            upside_text2 = frac_part  
            cont2 = 0  # Variable para almacenar la parte decimal convertida a decimal
            negative_raised = -1  # Exponente negativo de la base 8

            # Convierte la parte decimal del número octal en su representación decimal
            for j in upside_text2:
                j = int(j)
                cont2 += j * (8**negative_raised)  # Multiplica cada dígito por la potencia correspondiente de 8, pero con exponentes negativos
                negative_raised -= 1

            result = f'{cont + cont2}' if cont2 else str(cont)  # Combina la parte entera y decimal en el resultado final

        return result
    except ValueError:
        return "Ingrese un numero octal valido"


def hex_to_dec(hex_num):

    # Dividir el número en parte entera y parte fraccionaria
    int_part, frac_part = (hex_num.split('.') + ['0'])[:2]

    # Convertir la parte entera en valor absoluto y entero
    frac_dec = 0
    int_dec = abs(int(int_part, 16))
    for i, d in enumerate(frac_part):
        frac_dec += int(d, 16) / (16 ** (i+1))

    # Unir las dos partes para formar el resultado
    decimal = int_dec + frac_dec

    # Si no hay parte fraccionaria, retornar solo el entero
    if frac_dec == 0:
        decimal = int(decimal)

    # Para los números negativos
    if hex_num.startswith('-'):
        decimal = -decimal

    return decimal

def dec_to_hex(num):
    try:
        #Se define una lista de dígitos hexadecimales (digits) que se utilizará en la conversión
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

        # Dividir el número en parte entera y parte fraccionaria
        int_part, frac_part = (num.split('.') + ['0'])[:2]

        # Convertir la parte entera en valor absoluto y entero
        int_part = abs(int(int_part))

        # Convertir la parte fraccionaria en un número decimal
        frac_part = float('0.' + frac_part)

        # Convertir la parte entera a su representación hexadecimal
        hexa_entero = ''
        while int_part > 0:
            resto = int_part % 16
            hexa_entero = digits[resto] + hexa_entero
            int_part = int_part // 16

        # Convertir la parte fraccionaria a su representación hexadecimal
        hexa_fraccion = ''
        while frac_part != 0:
            frac_part *= 16
            digito = int(frac_part)
            hexa_fraccion += hex(digito).upper()[2:] #Me dio pereza hacer la parte decimal de una manera mas compleja asi que le puse un upper para dicimular xd
            frac_part -= digito

        # Combinar la parte entera y la parte fraccionaria en la representación hexadecimal completa
        hexadecimal = f'{hexa_entero}.{hexa_fraccion}' if hexa_fraccion else hexa_entero  # Combina la parte entera y decimal en el resultado final

        # Agrega el signo negativo al resultado si el número original es negativo
        if num.startswith('-'):
            hexadecimal = '-' + hexadecimal

        return hexadecimal
    except ValueError:
        return "Ingrece un numero decimal valido"