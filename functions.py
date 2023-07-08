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
    for i in num:
        print(i)