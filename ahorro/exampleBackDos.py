import math
import random


# lista_de_totales = [1, 5]

def cantidadFija(frecuencia, tiempo, meta):
    '''
    Ahorro en que cada ves que se ahorra es la misma cantidad
    tiempo entre meta igual a cantidad
    es entre frecuencia dentro de un tiempo especifico
    primero es cuantas frecuencias hay en el tiempo y de ahi sacar que cantidad en cada frecuencia
    t/m = C
    '''

    nfrecuencia = tiempo/frecuencia
    cantidad = meta/math.floor(nfrecuencia)
    cantidad = math.ceil(cantidad)
    print(nfrecuencia)
    print('Cantidad fija:', cantidad)

    
    return cantidad

cantidadFija(15, 365, 60000)

def sinLimiteDeTiempo(cantidad, frecuencia, meta):
    '''
     que pasa en el caso en el que el tiempo se define por la meta y lo que puedo ahorrar cada vez
    En este caso yo defino la cantidad que puedo ahorrar, y mi meta el tiempo es el que será variable
    m/c = T
    en este caso ahorras y ahorras hasta llegar a la meta, nada que deba llevar logica
    '''

    tiempo = meta/cantidad
    tiempo = math.ceil(tiempo)
    print(tiempo, 'pagos * la frecuencia')

    # ahorroIguales = 0
    return tiempo

sinLimiteDeTiempo(230, 1, 60000)

def libreSinTiempo(sumaCantidades, frecuencia, cantidad_variable, meta):
    '''
    Ahorro en el que cada vez que se ahorra es con una cantidad variable pero 
    la meta es la misma
    en este caso no hay tiempo?
    ahorras cuando te decimos pero ahorras lo que puedes ahorrar y nosotros te decimos cuando
    cumples te meta
    t = m/vC
    '''
    
    # sumaCantidades = 0

    if meta >= sumaCantidades:
        print('lograsteTuMeta')
    else:
        print('sigue ahorrando')    
        # cantidad_variable += cantidad_variable    
        # sumaCantidades = cantidad_variable

    # tiempo = meta / cantidad_variable
    # print(tiempo)
    # ahorroVariableMeta = 0
    return sumaCantidades
    


def ahorrarEsLaMeta(frecuencia, cantidad_variable):
    '''
    tu meta es ahorrar. ahorras con periodicidad pero sin una meta especifica
    ahorras una cantidad abierta, un porecntaje de sueldo o 
    tus ganancias pasivas
    aqui llevas el control de cuanto es lo que ahorras cada vez y cuanto es tu total
    en este caso estaria chido tener cantidad que se reste?
    '''
    
    cantidad_variable += cantidad_variable

    ahorroVariableNoMeta = 0
    return ahorroVariableNoMeta


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

    print("debug ERROR")
    print(lista_de_totales)
    # print(lista_de_totales[1])
    # print(clean_list[2])
    print(clean_list)
    print("MIAHORRO")    
    print(miAhorro)
    for ele in range(0, len(clean_list)):
        miAhorro = miAhorro + clean_list[ele]  
    print("MIAHORRO")    
    print(miAhorro)

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

    # print('numero clave', int(tiempo/frecuencia))
    # print('frecuencia:', frecuencia)
    # print('tiempo:', tiempo)
    # print('meta:', meta)
    # frecuencia = int(frecuencia)
    # meta = int(meta)
    # total = 0
    # maxN = 365
    maxN = 275
    mytotal = 0
    metaList = []
    cantidadList = []
    frecuencia = int(tiempo/frecuencia)
    # ahorroList = []

    posList = [0, 0, frecuencia/2, frecuencia-1]
    # print("posList:")
    # print(posList)
    # numDown = maxN/2
    ix = str(maxN)
    x = math.trunc(maxN / int(ix[0]))

    #creamos una lista length frecuencia index con 0 como valor
    for i in range(frecuencia):
        cantidadList.append(0*i)

    # print("originalListUNO:")
    # print(cantidadList)


    #tomamos la lista y le agregamos los valores en [posList] 
    for i in range(3+1):
        cantidadList[int(posList[i])]=(x*i)
        # print(cantidadList)

    cantidadList[0] = 10
    cantidadList[int(len(cantidadList)/2)] = int(meta/(tiempo/frecuencia))
    cantidadList[len(cantidadList)-1] = int(meta/(tiempo/frecuencia)*2)

    # print('METAENTREFRECUENCIA')
    # print(meta/frecuencia)

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

   
    cantidadList[0] = 10  
    while ototal < meta:
        for i in range(frecuencia):
            ototal+=100
            # print(i+1, "pero soy menor", ototal)
            cantidadList[i] = cantidadList[i]+100
           
    else:
        pass  

    ototal = 0
    for ele in range(0, len(cantidadList)):
        ototal = ototal + cantidadList[ele] 
    
    
    print("")
    print("")
    print("<><<><><><")
    print(ototal)
    print(cantidadList)
    print("")
    print("")

    remanent = 0

    if ototal < meta:
        remanent = meta - ototal
        print("menor que remanent", remanent)

    diferenceList = []
    recoveryList = []
    valorX = 0
    untotal = 0
    for ra in range(len(cantidadList)):
        recoveryList.append(int(cantidadList[len(cantidadList)-1]/len(cantidadList)))
        cantidadList[len(cantidadList)-1] = cantidadList[0]
        cantidadList[ra] = cantidadList[ra]+recoveryList[ra]

    # cantidadList.sort()

    while ototal > meta:
        print("WORKING")
        # print(recoveryList)
        for lp in range(len(cantidadList)):
            if cantidadList[lp] < 0:
                cantidadList[lp] = cantidadList[lp] + 1

        remanent = ototal - meta  
        print("remanent", remanent)
        
        print("")

        valorX = remanent/frecuencia

        diferenceList = []

        for i in range(frecuencia):
            diferenceList.append(math.trunc(valorX))

        print("first")
        print("DIF:", len(diferenceList), diferenceList)


        diferenceList = diferenceList[:frecuencia]

        # divergentList = []
        # for i in range(frecuencia):
        #     divergentList.append(diferenceList[i]+i+1)
        #     print('waitWhat what IS THIS', i)
        #     print(divergentList)
        untotal = 0    

        for ele in range(0, len(cantidadList)):
            untotal = untotal + cantidadList[ele]
            # print(untotal)            

           
        print('BEFORE', cantidadList)
        print("untotal antes de Tero:", untotal)

        # here is the magic??
        for i in range(frecuencia):
            if cantidadList[i] > diferenceList[i]:
                cantidadList[i] = cantidadList[i] - diferenceList[i]

        cototal = 0
        for ele in range(0, len(cantidadList)):
            cototal = cototal + cantidadList[ele]
            # print(cototal)            
  

        # ototal = 0
        # for ele in range(0, len(cantidadList)):
        #     ototal = ototal + cantidadList[ele]   
        # cantidadList.sort()

        print("")
        print('AFTER', cantidadList)
        print("untotal despuesd de COero:", cototal)
        
        ototal = untotal
        print("untotal antes de Oero:", ototal)

        # print('LOOKING', diferenceList)
        print("")

        


      

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
                # print("this IS METALIST")
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


                print("volvemos a empezar:")
                print("")
                print("|||")
                print("")

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

                print("aqui cuanto vale ototal", ototal)
                break



    # ototal = 0
    # for ele in range(0, len(diferenceList)):
    #     ototal = ototal + diferenceList[ele]
    # # print("saber cuanto vale el array", ele, ototal, len(diferenceList))
    # print("Ototal1:", ototal)


    # ototal = 0
    # for ele in range(0, len(cantidadList)):
    #     ototal = ototal + cantidadList[ele]
    # print("Ototal2:", ototal)

    # print("CANTIDADLIST") 
    # print(cantidadList)    
    # print("LENGTH", len(cantidadList))

  

    # for x in range(frecuencia):
    #     cantidadList.append(0 * x) 

    # mytotal = 0

    # for ele in range(0, len(cantidadList)):
    #     mytotal = mytotal + cantidadList[ele]    

  
    
    # print("antes de la resta de cantidadList en mytotal:", mytotal)
    # print(lTotales)






    # comented CLEAN_LIST ˘˘˘˘

    # restarLista = clean_list
    # print(restarLista)
    # print("@@@@@@------@@@@@@")

    # for lt in range(0, len(restarLista)):
    #     if not restarLista[lt] in cantidadList:
    #         print(restarLista[lt])
    #     else:       
    #         cantidadList.remove(restarLista[lt])

    # print("@@@@@@------@@@@@@")


    print("CANTIDAD LIST")
    print(cantidadList) 

    mytotal = 0

    for ele in range(0, len(cantidadList)):
        mytotal = mytotal + cantidadList[ele]    

  

    print("resuma de cantidadList:", ototal)
    print("resuma de cantidadList en mytotal:", mytotal)
    # print("resuma de total cantidadList:", total)
    print("")
    print("^^^^^^^^^")
    print("")
    print("")

    
    
    return cantidadList
    # pass


# sistema_Ahorro(365, 365, 365)


def restArray(originalList, restarLista):
    print(type(originalList), originalList)
    print('***restar lisa***')
    print(type(restarLista), restarLista)

    if len(originalList) <= 0:
        originalList = [0, 0] 


    if len(restarLista) <= 0:
        restarLista = [0, 0] 

    lPaso1 = str(restarLista)[1:-1]

    lPaso2 = lPaso1.replace('QuerySet', '').replace(' ', '').replace('[', '').replace(']', '').replace(':', '').replace('Ahorro', '').replace('<', '').replace('>', '')
  
    splitList = lPaso2.split (",")
 

    global clean_list
    clean_list = []
    
    for c in splitList:
        clean_list.append(int(c))


    print("(*)()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()")
    a = 1235456
    originalList = originalList.split(',')
    print(originalList)

    # originalList = originalList.replace('[', '').replace(']', '')
    paso_list = []
    for list in originalList:
        new_lis = list.replace('[', '').replace(']', '').replace("\'", "")
        paso_list.append(new_lis)

    # print(type(new_list))
    # print(originalList)
    print('-')
    new_list = []
    for list in paso_list:
        new = int(list)
        new_list.append(new)

    print("originalList es igual a newList", new_list)
    print("restar lista es igual a cleanLIst", clean_list)
    # t.lista_de_totales
    for lt in range(0, len(clean_list)):
        if not clean_list[lt] in new_list:
            print('anti EXISTENCIA')
            print(lt, new_list[1], clean_list[0])
        else:
            print('ERASER')
            print(clean_list[lt])
            new_list.remove(clean_list[lt])

    print(")()()()()()()()()()()()()(*)()()()()()()()()()()()()()()()()()(")

    print('')
    print('')
    print("MINUEVALISTA")
    print(new_list) 
    print('')
    
    print('¯˘¯˘¯˘¯˘¯˘¯˘¯˘¯˘¯˘¯˘¯˘¯˘¯˘¯˘¯˘¯˘¯˘¯˘¯˘¯˘¯˘')
    print('')
    return new_list