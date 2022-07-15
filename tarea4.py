res=int(input("Desea realizar una operacion? digite 1 para si, 0 para no\n"))
suma=[]
resta=[]
mult=[]
div=[]

while res!=0:
    ope=int(input("Operaciones:\n 1-suma\n 2-resta\n 3-multiplicaci'on\n 4-divisi'on\n 5-historial\n"))
    
    if ope==1:
        print("Ingrese dos n'umeros:\n")
        n=float(input())
        m=float(input())
        suma.append(n)
        suma.append(m)
        suma.append(n+m)
        print("suma: ", suma[0], "+", suma[1], "=", suma[2],"\n")
        res=int(input("Desea realizar otra operacion? digite 1 para si, 0 para no\n"))

    elif ope==2:
        print("Ingrese dos n'umeros:\n")
        n=float(input())
        m=float(input())
        resta.append(n)
        resta.append(m)
        resta.append(n-m)
        print("resta: ", resta[0], "-", resta[1], "=", resta[2],"\n")
        res=int(input("Desea realizar otra operacion? digite 1 para si, 0 para no\n"))
    elif ope==3:
        print("Ingrese dos n'umeros:\n")
        n=float(input())
        m=float(input())
        mult.append(n)
        mult.append(m)
        mult.append(n*m)
        print("multiplicaci'on: ", mult[0], "*", mult[1], "=", mult[2],"\n")
        res=int(input("Desea realizar otra operaci'on? digite 1 para si, 0 para no\n"))
    elif ope==4:
        print("Ingrese dos n'umeros:\n")
        n=float(input())
        m=float(input())
        div.append(n)
        div.append(m)
        div.append(n/m)
        print("divisi'on: ", div[0], "/", div[1], "=", div[2],"\n")
        res=int(input("Desea realizar otra operaci'on? digite 1 para si, 0 para no\n"))
    elif ope==5:
        if len(suma)==0 & len(resta)==0 & len(mult)==0 & len(div)==0:
            print("Historial vaci'o \n")
            
        else:
            if len(suma)!=0:
                print("suma: ", suma[0], "+", suma[1], "=", suma[2],"\n")
            if len(resta)!=0:
                print("resta: ", resta[0], "-", resta[1], "=", resta[2],"\n")
            if len(mult)!=0:
                print("multiplicaci'on: ", mult[0], "*", mult[1], "=", mult[2],"\n")
            if len(div)!=0:
                print("divisi'on: ", div[0], "/", div[1], "=", div[2],"\n")
            p=int(input("Desea borrar el historial? 1-Si, 2-No\n"))
            if p==1:
                suma.clear()
                resta.clear()
                mult.clear()
                div.clear()
        res=int(input("Desea realizar otra operaci'on? digite 1 para si, 0 para no\n"))


