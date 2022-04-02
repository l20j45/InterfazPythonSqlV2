contador=0
file = open('fechasAcomodadas.txt','w')
with open('fechas.txt', 'r') as f:
    for linea in f:
        print(linea)
        linea=linea.rstrip('\n')
        contador+=1
        if "/" in linea:
            parametro=linea.split("/")
            fechaNueva=""+parametro[2]+"-"+parametro[1]+"-"+parametro[0]
        elif "-" in linea: 
            parametro=linea.split("-")            
            fechaNueva="20"+parametro[2]+"-"+parametro[0]+"-"+parametro[1]
        else:
            fechaNueva="2022-03-01"
        file.write(fechaNueva)
        file.write("\n")
    print(contador)
