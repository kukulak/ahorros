import math
import random


fthislist = ["apple", "banana", "cherry", "apple", "cherry"]
thislist = []
total = 0
mylist = [348, 88, 88]

testList=[]
finalList=[]

frecuencia = 52
frecuencia = 12
tiempo = 365
meta = 9000
ahorrado = 0

cantidades = meta / frecuencia


valores = 0
process = 0



while ahorrado < meta:
    
    ahorrado += 500

for x in range(frecuencia):
    cantidades = meta / frecuencia
    valores = math.ceil(cantidades)*2
    process += meta - valores
    testList.append(math.ceil(valores))
    finalList.append(math.ceil(x))
   
    meta -= valores
  

someList = [0, 0, 15, 25, 30, 45, 50]*len(testList)
restList =  len(someList) - len(testList)

someList = someList[:-restList]
ll = len(someList)


zipped_lists = zip(testList, someList)
listResult = [x + y for (x, y) in zipped_lists]



listResult.sort(reverse=True)


for x in range(366):
  thislist.append(x)

  
print(listResult)


for ele in range(0, len(listResult)):
    total = total + listResult[ele]

remananent = 0

if total < meta:
    remanent = meta - total


 
	## printing total value
# print("Sum of all elements in given list: ", total)


# frecuencia = 52
# tiempo = 365
# meta = 9000
# maxN = 300 
# minN = 5

def sistema_Ahorro(frecuencia, tiempo, meta, maxN, minN):
    """
    Create a list in range of min and max
    of frecuencia in time,
    whith exactly length of frecuencia divided by tiempo
    and the sume of values limited by meta
    """
    print('frecuencia:', frecuencia)
    print('tiempo:', tiempo)
    print('meta:', meta)
    print('maxN:', maxN)
    print('minN:', minN)

    total = 0
    mytotal = 0
    metaList = []
    ahorroList = []
    cantidadList = []
    secondList = []
    cantidad = 0
    posList = [0, 0, frecuencia/2, frecuencia-1]
    numDown = maxN/2
    ix = str(maxN)
    x = math.trunc(maxN / int(ix[0]))

    for i in range(frecuencia):
        cantidadList.append(0*i)

    for i in range(3+1):
        cantidadList[int(posList[i])]=(x*i)

    for i in range(frecuencia):
        if cantidadList[i] == 0:
            cantidadList[i] = cantidadList[i-1]+1

  
    print("originalList:", cantidadList)

    # for ele in range(0, len(cantidadList)):
    #     mytotal = mytotal + cantidadList[ele] 

    # print("originalList:")
    # print(cantidadList)
    # print("originalList LENGTH:", len(cantidadList), ", con la suma:",mytotal)

    ototal = 0
    utotal = 0
    
    res = list(filter(lambda x : x > 0, cantidadList))
    
    
    for ele in range(0, len(cantidadList)):
        ototal = ototal + cantidadList[ele] 

    for ele in range(0, len(res)):
        utotal = utotal + res[ele]      

    while ototal < meta:
        for i in range(frecuencia):
           
            ototal+=1
            cantidadList[i] = cantidadList[i]+1
           
    else:
        pass  

    numero = 0

        
    ototal = 0
    for ele in range(0, len(cantidadList)):
        ototal = ototal + cantidadList[ele] 
    
    remanent = 0

    if ototal < meta:
        remanent = meta - ototal
        print("menor que remanent", remanent)

    diferenceList = []
    valorX = 0
    untotal = 0
    while ototal > meta:
        remanent = ototal - meta  
        print("mayor que remanent", remanent)
        valorX = remanent/frecuencia
        diferenceList = []
        for i in range(frecuencia):
            diferenceList.append(math.trunc(valorX))
        diferenceList = diferenceList[:frecuencia]
        print("diferenciList:", diferenceList)
        for i in range(frecuencia):
            if cantidadList[i] > diferenceList[i]:
                cantidadList[i] = cantidadList[i] - diferenceList[i]
           
        untotal = 0    
        for ele in range(0, len(cantidadList)):
            untotal = untotal + cantidadList[ele]
        print("untotal", untotal)
        ototal = untotal
        if diferenceList[int(len(diferenceList)/2)] == 0:
            for i in range(remanent):
                metaList.append(1)
            
            metaList.extend(diferenceList) 
            metaList = metaList[:frecuencia]
            
            cantidadList.sort(reverse=True)
            for i in range(frecuencia):
                if cantidadList[i] > metaList[i]:
                    cantidadList[i] = cantidadList[i] - metaList[i]
            print("meta LIST:", metaList)
            print("meta LIST:", len(metaList))
            print("finale remanent:", remanent)
            break


    ototal = 0
    for ele in range(0, len(diferenceList)):
        ototal = ototal + diferenceList[ele]
    print("saber cuanto vale el array", ele, ototal, len(diferenceList))

    ototal = 0
    for ele in range(0, len(cantidadList)):
        ototal = ototal + cantidadList[ele]


  
    print("CANTIDADLIST", cantidadList)    
    print("LENGTH", len(cantidadList))
    print("pero pero", x)
  

    for x in range(frecuencia):
        cantidadList.append(0 * x) 


   

    for ele in range(0, len(ahorroList)):
        total = total + ahorroList[ele]

    for ele in range(0, len(cantidadList)):
        mytotal = mytotal + cantidadList[ele]    

  
    position = numDown
    positiond = maxN 

  

 
    # print("cantidadList", cantidadList)
    # print("secondList", secondList)
    # print("suma de cantidadList?", mytotal)
    print("resuma de cantidadList:", ototal)
    print("resuma de cantidadList sin negativos:", utotal)
    # print(ahorroList)
    # print(total)
    # print(len(ahorroList))
    # print(metaList)
 

    pass


sistema_Ahorro(365, 365, 365, 365, 365)