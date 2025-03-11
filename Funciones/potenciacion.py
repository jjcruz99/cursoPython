print("            Potenciacion    a^n")

def potencia(base, exponente):
    if exponente == 0 :
        return  1
    else :
       return base * potencia(base,exponente=exponente - 1)


if __name__ == '__main__':
    base = int(input("Digite la base : "))
    exp = int(input("Digite el exponente "))
    print(potencia(base=base,exponente=exp))