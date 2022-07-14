verdura={"Brocoli":8.55, "Pepino":6.87, "Calabaza":11.55, "Chayote":14.33}
ver=input("Qu'e verdura busca?\n")

if ver in verdura:
    k=float(input("N'umero de kilos\n"))
    res=verdura[ver]*k
    print(k,"kilos de ", ver," valen ", res, "pesos")

else:
    print("Lo siento, por el momento no contamos con esa verdura")
