def par_ou_impar(num: int) -> str:
    sobra = num % 2

    match sobra:
        case 0:
            return 'par'
        case 1:
            return 'impar'

def classificar_number(num: int): 
    if num < 0:
        return 'negativo'
    elif num == 0:
        return 'zero'
    elif 11 <= num <= 100:
        return 'médio'
    else:
        return 'grande'