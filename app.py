def par_ou_impar(num: int) -> str:
    sobra = num % 2

    match sobra:
        case 0:
            return 'par'
        case 1:
            return 'impar'