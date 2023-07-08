def dec_to_bin(num):
    if num == 0:
        return '0'
    
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2  
    return binary

def frac_to_bin(num):
    frac = float(f'0.{num}')
    result = ''
    cont = 0
    while frac != 0 and cont != 7:
        temp = str(frac * 2).split('.')
        result = result + str(temp[0])
        frac = float('0.'+temp[1])
        #print(frac)
        cont+=1
    return result

def bin_to_dec(num):
    cont = 0
    raised = 0
    upside_text = num[::-1]
    for i in upside_text:
        i = int(i)
        cont += i * (2**raised)
        raised += 1
        #print(cont)
    return cont