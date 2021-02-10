import math
import random


# lista_de_totales = [1, 5]

#sacar la lista de las cantidades ahorradas y el total
def Lista_total(lista_de_totales):
    """obtenemos los ahorros y los transformamos en una lista
    despues sumamos el total de esa lista, 
    aparte tomamos la lista original y le restamos los numeros
    de la lista total que disminuira su tamaño
    """
    # def __init__(self, lista_de_totales):
        # self.lista_de_totales = lista_de_totales
    # lista_de_totales = lista_de_totales
        
        # self.ahorros = ahorros

        # for a in ahorros:
        #     lista_de_totales.append(a)
    # lista_de_totales = [1, 5]

    if len(lista_de_totales) <= 0:
        lista_de_totales = [0, 0] 

    global lTotales 
    lTotales = lista_de_totales

    lPaso1 = str(lista_de_totales)[1:-1]

    # print(lPaso1)

    # lPaso2 = {x.replace('QuerySet', '').replace('Ahorro', '') for x in lPaso1}
    lPaso2 = lPaso1.replace('QuerySet', '').replace(' ', '').replace('[', '').replace(']', '').replace(':', '').replace('Ahorro', '').replace('<', '').replace('>', '')
    # lPaso3 = lPaso2.replace(' ', '')
    # lPaso3 = lPaso3.replace('[', '')

    # print(lPaso2)

    splitList = lPaso2.split (",")
    # print("list: ", splitList)

    global clean_list
    clean_list = []
    
    for c in splitList:
        clean_list.append(int(c))
    # list(lista_de_totales.fetchall())
    
    # for cl in range(len(lista_de_totales)):
    #     clean_list.append(lista_de_totales[cl])


    miAhorro = 0
    # print("debug ERROR")
    # print(lista_de_totales)
    # print(lista_de_totales[1])
    # print(clean_list[2])
    # print(clean_list)

    for ele in range(0, len(clean_list)):
        miAhorro = miAhorro + clean_list[ele]  

    return miAhorro
# def totals():
#     lista_de_totales = [1, 5]
#     return Lista_total(lista_de_totales)

# t = totals()    
# print(t)    
# Lista_total([1, 5])
# print("")
# print('DALE AHORROS TU PUEDES')
# print("")
# print(Lista_total(lista_de_totales))


# def sistema_Ahorro(frecuencia, tiempo, meta, maxN, minN):
def sistema_Ahorro(frecuencia, tiempo, meta):
    """
    Create a list in range of min and max
    of frecuencia in time,
    whith exactly length of frecuencia divided by tiempo
    and the sume of values limited by meta
    """

    # if meta.isalnum:
    #     pass
    # else:
    #     ''.join(e for e in meta if e.isalnum)
    #     print('aqui vamos otra vez')
    #     print(meta)

    print('numero clave', int(tiempo/frecuencia))
    print('frecuencia:', frecuencia)
    print('tiempo:', tiempo)
    print('meta:', meta)
    # frecuencia = int(frecuencia)
    # meta = int(meta)
    # total = 0
    maxN = 365
    mytotal = 0
    metaList = []
    cantidadList = []
    frecuencia = int(tiempo/frecuencia)
    # ahorroList = []

    posList = [0, 0, frecuencia/2, frecuencia-1]
    # numDown = maxN/2
    ix = str(maxN)
    x = math.trunc(maxN / int(ix[0]))

    #creamos una lista length frecuancia index con 0 como valor
    for i in range(frecuencia):
        cantidadList.append(0*i)

    # print("originalListUNO:")
    # print(cantidadList)


    #tomamos la lista y le gregamos los valores en [posList] 
    for i in range(3+1):
        cantidadList[int(posList[i])]=(x*i)

    # print("originalListDOS:")
    # print(cantidadList)

    #lista llena de valores diferentes a cero, entre los valores resultantes de posList
    for i in range(frecuencia):
        if cantidadList[i] == 0:
            cantidadList[i] = cantidadList[i-1]+1

    # print("originalListTRES:")
    # print(cantidadList)

    #sumamos todos los valores de la lista para ver que tenemos que hacer
    for ele in range(0, len(cantidadList)):
        mytotal = mytotal + cantidadList[ele]    
  
    # print("originalListCUATRO:")
    # print(mytotal)
    # print("originalList LENGTH:", len(cantidadList), ", con la suma:",mytotal)
    
    ototal = 0
    for ele in range(0, len(cantidadList)):
        ototal = ototal + cantidadList[ele] 


    while ototal < meta:
        # print("pero soy menor", ototal)
        for i in range(frecuencia):
            ototal+=1
            cantidadList[i] = cantidadList[i]+1
           
    else:
        pass  

        
    ototal = 0
    for ele in range(0, len(cantidadList)):
        ototal = ototal + cantidadList[ele] 
    
    remanent = 0

    if ototal < meta:
        remanent = meta - ototal
        # print("menor que remanent", remanent)

    diferenceList = []
    valorX = 0
    untotal = 0
    while ototal > meta:
        remanent = ototal - meta  
        
        # print("mayor que remanent", remanent)
        # print("")

        valorX = remanent/frecuencia

        diferenceList = []

        for i in range(frecuencia):
            diferenceList.append(math.trunc(valorX))

        diferenceList = diferenceList[:frecuencia]
        # print("diferenciList:", diferenceList)

        for i in range(frecuencia):
            if cantidadList[i] > diferenceList[i]:
                cantidadList[i] = cantidadList[i] - diferenceList[i]
           
        untotal = 0    
        for ele in range(0, len(cantidadList)):
            untotal = untotal + cantidadList[ele]
        ototal = untotal

        # print("untotal antes de cero:", untotal)
        # print("")

        if diferenceList[0] == 0:
            while ototal>meta:

                untotal = 0    
                for ele in range(0, len(cantidadList)):
                    untotal = untotal + cantidadList[ele]
                cantidadList.sort(reverse=True)

                # print("LISTA EN PROCESO - con estos valores:")
                # print(cantidadList)
                # print("la suma de la lista es:")
                # print(untotal)
                # print("me falta esto:", remanent)

                metaList.clear()
                for i in range(remanent):
                    metaList.append(1)
                

                metaList.extend(diferenceList) 
                metaList = metaList[:frecuencia]
                # print(metaList)
                
                for i in range(frecuencia):
                    if cantidadList[i] > metaList[i]:
                        cantidadList[i] = cantidadList[i] - metaList[i]
                
                untotal = 0    
                for ele in range(0, len(cantidadList)):
                    untotal = untotal + cantidadList[ele]

                # print("untotal dentro de ==", untotal)

                ototal = untotal

                # print("meta LIST:", metaList)
                # print("meta LIST LENGTH:", len(metaList))
                # print("almost finale remanent:", remanent)
                # print("aqui cuanto vale ototal", ototal)

                # if ototal>meta:
                # print("agan")
                # print(remanent)
                # print("-")
                remanent = ototal - meta
                if remanent < 0:
                    remanent = 0
                    
                # print(remanent)
                # print("-")
                # remanent = abs(remanent)
                # print("-")
                # print(remanent)


                # print("volvemos a empezar:")
                # print("")
                # print("|||")
                # print("")

                metaList.clear()
                
                for i in range(remanent):
                    metaList.append(1)
                    # break
                metaList.extend(diferenceList) 
                metaList = metaList[:frecuencia]
                
                # print("meta LIST:", metaList)
                # print("meta LIST LENGTH:", len(metaList))

                for i in range(frecuencia):
                    if cantidadList[i] > metaList[i]:
                        cantidadList[i] = cantidadList[i] - metaList[i]
                        break
                    break
                
                untotal = 0   
                 
                for ele in range(0, len(cantidadList)):
                    untotal = untotal + cantidadList[ele]

                ototal = untotal    

                
                # print("")
                # print("finale remanent:", remanent)
                # print("")

                # print("aqui cuanto vale ototal", ototal)
                break


    ototal = 0
    for ele in range(0, len(diferenceList)):
        ototal = ototal + diferenceList[ele]
    # print("saber cuanto vale el array", ele, ototal, len(diferenceList))

    ototal = 0
    for ele in range(0, len(cantidadList)):
        ototal = ototal + cantidadList[ele]

    # print("CANTIDADLIST") 
    # print(cantidadList)    
    # print("LENGTH", len(cantidadList))

  

    # for x in range(frecuencia):
    #     cantidadList.append(0 * x) 

    mytotal = 0

    for ele in range(0, len(cantidadList)):
        mytotal = mytotal + cantidadList[ele]    

  
    
    # print("antes de la resta de cantidadList en mytotal:", mytotal)
    # print(lTotales)
    restarLista = clean_list
    # print(restarLista)
    # print("@@@@@@------@@@@@@")

    # t.lista_de_totales
    for lt in range(0, len(restarLista)):
        if not restarLista[lt] in cantidadList:
            # print('anti EXISTENCIA')
            print(restarLista[lt])
        else:
            # print(restarLista[lt])
            cantidadList.remove(restarLista[lt])

    # print("@@@@@@------@@@@@@")

    # print(cantidadList) 

    mytotal = 0

    for ele in range(0, len(cantidadList)):
        mytotal = mytotal + cantidadList[ele]    

  

    # print("resuma de cantidadList:", ototal)
    # print("resuma de cantidadList en mytotal:", mytotal)
    # print("resuma de total cantidadList:", total)
    print("")
    print("^^^^^^^^^")
    print("")
    print("")

    
    
    return cantidadList
    # pass


# sistema_Ahorro(365, 365, 365)