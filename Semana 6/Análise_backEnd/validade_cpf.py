def valido(g):
    b = str(g)
    a = 0
    d = 0
    if len(b) == 11:
        c = list(b)

        if b[0]:
            c[0] = str(int(b[0])*10)
        if b[1]:
            c[1] = str(int(b[1])*9)
        if b[2]:
            c[2] = str(int(b[2])*8)
        if b[3]:
            c[3] = str(int(b[3])*7)
        if b[4]:
            c[4] = str(int(b[4])*6)
        if b[5]:
            c[5] = str(int(b[5])*5)
        if b[6]:
            c[6] = str(int(b[6])*4)
        if b[7]:
            c[7] = str(int(b[7])*3)
        if b[8]:
            c[8] = str(int(b[8])*2)

        cont = 0
        for j in range(9):
            cont += int(c[j])
        
    
        if str((cont*10)%11) == b[-2]:
            d += 1
##        else:
##            print("inválido")

        
        if b[0]:
            c[0] = str(int(b[0])*11)
        if b[1]:
            c[1] = str(int(b[1])*10)
        if b[2]:
            c[2] = str(int(b[2])*9)
        if b[3]:
            c[3] = str(int(b[3])*8)
        if b[4]:
            c[4] = str(int(b[4])*7)
        if b[5]:
            c[5] = str(int(b[5])*6)
        if b[6]:
            c[6] = str(int(b[6])*5)
        if b[7]:
            c[7] = str(int(b[7])*4)
        if b[8]:
            c[8] = str(int(b[8])*3)
        if b[9]:
            c[9] = str(int(b[9])*2)

        cont = 0
        for j in range(10):
            cont += int(c[j])

        e = str((cont*10)%11)
        if e[-1] == b[-1]:
            d += 1
##        else:
##            print("inválido")


        for i in range(len(b)-1):
            if b[i] == b[i+1]:
                a += 1
        #return a

        if d == 2 and a != 10:
            return "válido"
        else:
            return "inválido"


#######################################################
##b = '06887037637'
##c = list(b)
##
##if b[0]:
##    c[0] = str(int(b[0])*10)
##if b[1]:
##    c[1] = str(int(b[1])*9)
##if b[2]:
##    c[2] = str(int(b[2])*8)
##if b[3]:
##    c[3] = str(int(b[3])*7)
##if b[4]:
##    c[4] = str(int(b[4])*6)
##if b[5]:
##    c[5] = str(int(b[5])*5)
##if b[6]:
##    c[6] = str(int(b[6])*4)
##if b[7]:
##    c[7] = str(int(b[7])*3)
##if b[8]:
##    c[8] = str(int(b[8])*2)
##
##cont = 0
##for j in range(9):
##    cont += int(c[j])
##
##if str((cont*10)%11) == b[-2]:
##    print("primeiro dígito válido")
##else:
##    print("inválido")

######################################################
##    b = '06887037637'
##c = list(b)
##
##if b[0]:
##    c[0] = str(int(b[0])*11)
##if b[1]:
##    c[1] = str(int(b[1])*10)
##if b[2]:
##    c[2] = str(int(b[2])*9)
##if b[3]:
##    c[3] = str(int(b[3])*8)
##if b[4]:
##    c[4] = str(int(b[4])*7)
##if b[5]:
##    c[5] = str(int(b[5])*6)
##if b[6]:
##    c[6] = str(int(b[6])*5)
##if b[7]:
##    c[7] = str(int(b[7])*4)
##if b[8]:
##    c[8] = str(int(b[8])*3)
##if b[9]:
##    c[9] = str(int(b[9])*2)
##
##cont = 0
##for j in range(10):
##    cont += int(c[j])
##
##if str((cont*10)%11) == b[-1]:
##    print("segundo dígito válido")
##else:
##    print("inválido")
