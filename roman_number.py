nr=[
    (1000,'M'), (500, 'D'),
    (100,'C'), (50,'L'),
    (10,'X'), (5,'V'),(1,'I')
    ]

def roman_number(numero):
    numero="{:0>4d}".format(numero)
    Nlista=list(numero)

    millares=int(Nlista[0])
    centenas=int(Nlista[1])
    decenas=int(Nlista[2])
    unidades=int(Nlista[3])
    nu=""
    nd=""
    nc=""
    nm=""
    #unidades
    if unidades<9 and unidades>=5:
        nu=(nr[5][1]+(unidades-5)*nr[6][1])
    elif unidades<4:
        nu=(unidades*nr[6][1])
    elif unidades==4:
        nu='IV'
    elif unidades==9:
        nu='IX'
    #decenas
    if decenas<9 and decenas>=5:
        nd=(nr[3][1]+((decenas-5)*nr[4][1]))
    elif decenas>=1 and decenas<4:
        nd=(nr[4][1])*decenas
    elif decenas==4:
        nd='XL'
    elif decenas==9:
        nd='XC'   
    #centenas
    if centenas<9 and centenas>=5:
        nc=(nr[1][1]+(centenas-5)*nr[2][1])
    elif centenas>=1 and centenas<4:
        nc=(nr[2][1])*centenas
    elif centenas==4:
        nc='CD'
    elif centenas==9:
        nc='CM'
    #millares
    if millares>=1 and millares<4:
        nm=(nr[0][1])*millares   
    if int(numero)>=4000:
        print('Tas pasado')
    else:
        numero=(nm+nc+nd+nu)
        return numero




