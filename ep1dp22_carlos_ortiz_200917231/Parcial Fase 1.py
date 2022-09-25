import time
print ("---------------------")
print (" Carlos Ortiz Serrano")
print (" Carnet 200917231")
print (" Lic. en Informatica")
print (" ---------------------" )
print ("P A R C I A L No. 1")

def parcial():
    lista=[]
    print ("Solicitar 4 Textos")
    for inicio in range(4):
        texto=input("Ingrese un texto:")
        lista.append(texto)
    print("\nLos elementos ingresados son:", lista)

    print("--INDICAR CUAL DE LOS TEXTOS POSEE MENOR CARACTERES--")
   
    texto_1=(lista[0])
    texto_2=(lista[1])
    texto_3=(lista[2])
    texto_4=(lista[3])

    if (len(texto_1)==(len(texto_2)or len(texto_1)==(len(texto_3)or len(texto_1)==(len(texto_4))))):
        print ("Aplicacion no contenmpla IGUALDAD\n ")
    else:
        if (len(texto_2)==(len(texto_3)or len(texto_2)==(len(texto_4)or len(texto_2)==(len(texto_1))))):
            print ("Aplicacion no contenmpla IGUALDAD\n ")
        else:
            if (len(texto_3)==(len(texto_1)or len(texto_3)==(len(texto_2)or len(texto_3)==(len(texto_4))))):
                print ("Aplicacion no contenmpla IGUALDAD\n ")
            else:
                if (len(texto_4)==(len(texto_3)or len(texto_4)==(len(texto_2)or len(texto_4)==(len(texto_1))))):
                    print ("Aplicacion no contenmpla IGUALDAD\n ")
                else:
                    if (len(texto_1)<len(texto_2)and len(texto_1)<len(texto_3)and len(texto_1)<len(texto_4)):
                        print ("El texto con menos caracteres es:", texto_1)
                        
                    if (len(texto_2)<len(texto_1)and len(texto_2)<len(texto_3)and len(texto_2)<len(texto_4)):
                        print ("El texto con menos caracteres es:", texto_2)
                        
                    if (len(texto_3)<len(texto_4)and len(texto_3)<len(texto_1)and len(texto_3)<len(texto_2)):
                        print ("El texto con menos caracteres es:", texto_3)
                        
                    if (len(texto_4)<len(texto_3)and len(texto_4)<len(texto_2)and len(texto_4)<len(texto_1)):
                        print ("El texto con menos caracteres es:", texto_4)
                        
    print("\n--TEXTO MAYOR Ó MENOR, EN RELACION DEL ELEMENTO 2 Y 3--")

    if (len(lista[1]))>(len(lista[2])):
        print ((lista[1]),"es el texto  mayor\n")
    else:
        print ((lista[2]),"es el texto mayor\n")

    print("--MOSTRAR LA SUMA DE LONGITUDES--")
    contador=0
    promedio=0
    for lista in lista:
        print ("No.de letras del textoo:",lista,"es  :",len(lista))
        for lista in lista:
            contador+=1
    print ("Suma de todas las longitudes es:",contador)

     
#generar ejecucion
parcial()
duracion = 10
time.sleep(duracion)
exit()
