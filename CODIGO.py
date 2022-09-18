#Nombre del programador
print('''

                                          Programado por:
                                             NAVI_20
                  
''')


import math


opcion=0
while True:
    print('''
{--------------------------DIME QUE QUIERES CALCULAR--------------------------}
    
    -FɪSɪᴄᴀ-
    1->ACELERACION
    2->VELOCIDAD MEDIA
    3->DISTANCIA 
    4->VELOCIDAD FINAL
    5->FUERZA
    6->DENSIDAD
    7->MASA
    8->VOLUMEN
    
    -ᴛᴇᴄɴᴏʟᴏɢɪᴀ-
    9->LEY OHM(RESISTENCIA)
    10->LEY OHM(INTENSIDAD)
    11->LEY OHM(VOLTAJE)
    12->POLEA MOVIL
    
    -ᴍᴀᴛᴇᴍᴀᴛɪᴄᴀS-
    13->PITAGORAS(CON HIPOTENUSA Y UN CATETO)
    14->PITAGORAS(CON 2 CATETO)
    15->PERIMETRO Y AREA DEL CUADRADO
    16->PERIMETRO Y AREA DEL RECTANGULO
    17->PERIMETRO DEL TRIANGULO
    18->AREA DEL TRIANGULO
    19->PERIMETRO DEL ROMBO
    20->AREA DEL ROMBO
    21->PERIMETRO DEL PARALELOGRAMO
    22->AREA DEL PARALELOGRAMO
    23->PERIMETRO DEL TRAPECIO
    24->AREA DEL TRAPECIO
    25->PERIMETRO POLIGONO REGULAR
    26->PERIMETRO DEL CIRCULO
    27->AREA DEL CIRCULO
    28->AREA DEL CILINDRO
    29->VOLUMEN DEL CILINDRO
    30->AREA DE LA ESFERA
    31->VOLUMEN DE LA ESFERA
    32->AREA DEL CONO
    33->VOLUMEN DEL CONO
    34->AREA DEL CUBO
    35->VOLUMEN DEL AREA
       ''')



    opcion=int(input('Elige una opcion:'))

#FISICA

    if opcion == 1:
        print('')
        numero1=float(input('V.Inicial:'))
        numero2=float(input('Segundos:'))
        numero3=float(input('V.Final:'))
        print('RESULTADO: La aceleracion es igual a ',(numero3-numero1)/numero2,)
        
    elif opcion== 2:
        print('')
        numero3=float(input('Distancia total recorrida:'))
        numero4=float(input('Tiempo:'))
        print('RESULTADO: De la velocidad media es igual a ',numero3/numero4,)        

    elif opcion== 3:
        print('')
        numero5=float(input('VELOCIDAD:'))
        numero6=float(input('TIEMPO:'))
        print('RESULTADO: De la distancia ',numero5*numero6,)        

    elif opcion== 4:
        print('')
        numero7=float(input('ACELERACION:'))
        numero8=float(input('TIEMPO:'))
        print('RESULTADO: Velocidad final igual a ',numero7*numero8,) 
    
    elif opcion== 5:
        
        print('')
        numero9=float(input('MASA:'))
        print('RESULTADO:De la fuerza es:',numero9*9.81,)
    
    elif opcion== 6:
        print('')
        numero7=float(input('MASA:'))
        numero8=float(input('VOLUMEN:'))
        print('RESULTADO: Densidad igual a ',numero7/numero8,)

    elif opcion== 7:
        print('')
        numero7=float(input('VOLUMEN:'))
        numero8=float(input('DENSIDAD:'))
        print('RESULTADO: Masa igual a ',numero7*numero8,) 

    elif opcion== 8:
        print('')
        numero7=float(input('MASA:'))
        numero8=float(input('DENSIDAD:'))
        print('RESULTADO: Volumen igual a ',numero7/numero8,) 

    
    
#TECNOLOGIA

    elif opcion== 9:
        print('')
        numero7=float(input('VOLTAJE:'))
        numero8=float(input('AMPERIOS/INTENSIDAD:'))
        print('RESULTADO: Resistencia en la ley de ohm es igual a ',numero7/numero8,' ohmnios') 

    elif opcion== 10:
        print('')
        numero7=float(input('VOLTAJE:'))
        numero8=float(input('RESISTENCIA/OHMNIOS:'))
        print('RESULTADO: Intensidad de la ley de ohm igual a ',numero7/numero8,' amperios') 
    
    elif opcion== 11:
        print('')
        numero7=float(input('AMPERIO/INTENSIDAD:'))
        numero8=float(input('RESISTENCIA/OHMNIOS:'))
        print('RESULTADO: Voltaje de la ley de ohm igual a ',numero7*numero8,' voltios') 
    
    elif opcion == 12:
        print('')
        numero10 = float(input("RESISITENCIA: ") )
        print('RESULTADO:Fuerza necesaria es ',numero10/2, 'NEWTONS')

#MATEMATICAS

    elif opcion == 13:
        print('')
        numero7=float(input('HIPOTENUSA:'))
        numero8=float(input('CATETO:'))
        hipotenusa2=numero7*numero7
        cateto2=numero8*numero8
        Resultado = hipotenusa2-cateto2 
        print('RESULTADO: El cateto sobrante es ',Resultado, )

    elif opcion == 14:
        print('')
        numero7=float(input('CATETO1:'))
        numero8=float(input('CATETO2:'))
        cateto1=numero7*numero7
        cateto2=numero8*numero8
        Resultado= cateto1+cateto2
        RESULTADO=math.sqrt(Resultado)
        print('RESULTADO: La hipotenusa es ',RESULTADO)

    elif opcion == 15:
        print('')
        numero7=float(input('LADO:'))
        print('RESULTADO: El perimetro es ',numero7*4,)
        print('RESULTADO: El area es ',numero7*numero7,)
    
    
    elif opcion == 16:
        print('')
        numero7=float(input('LADO1:'))
        numero8=float(input('LADO2:'))
        print('RESULTADO: El perimetro es ',(2*numero7)+(2*numero8),)
        print('RESULTADO: El area es ',numero7*numero8,)
    
    elif opcion == 17:
        print('')
        numero7=float(input('LADO1:'))
        numero8=float(input('LADO2:'))
        numero9=float(input('LADO3:'))
        print('RESULTADO: El perimetro es ',numero7+numero8+numero9,)
    
    elif opcion== 18:
        print('')
        numero7=float(input('LADO DE ABAJO:'))
        numero9=float(input('ALTURA:'))
        print('RESULTADO: El area es ',(numero7*numero9)/2 ) 
    
    elif opcion== 19:
        print('')
        numero7=float(input('LADO:'))
        print('RESULTADO: El perimetro es ',numero7*4,) 
    
    elif opcion== 20:
        print('')
        numero7=float(input('DISTANCIA DESDE UNA ESQUINA AL CENTRO DESDE ABAJO:'))
        numero9=float(input('DISTANCIA DESDE UNA ESQUINA AL CENTRO DESDE ARRIBA:'))
        print('RESULTADO: El area es ',(numero7*numero9)/2 ) 

    elif opcion== 21:
        print('')
        numero7=float(input('LADO DE ARRIBA O DE ABAJO:'))
        numero9=float(input('LADO DE LOS LADOS:'))
        print('RESULTADO: El perimetro es ',(2*numero9)+(2*numero7) ) 

    elif opcion== 22:
        print('')
        numero7=float(input('LADO DE ARRIBA O DE ABAJO:'))
        numero9=float(input('ALTURA(si no la sabes debes hacer pitagoras NUM:13 o 14):'))
        print('RESULTADO: El area es ',numero7*numero9 ) 

    elif opcion== 23:
        print('')
        numero7=float(input('LADO1:'))
        numero9=float(input('LADO2:'))
        numero8=float(input('LADO3:'))
        numero6=float(input('LADO4:'))
        print('RESULTADO: El perimetro es ',numero7+numero9+numero6+numero8, ) 

    elif opcion== 24:
        print('')
        numero7=float(input('LADO DE ARRIBA:'))
        numero6=float(input('LADO DE ABAJO:'))
        numero8=float(input('ALTURA(si no la sabes debes hacer pitagoras NUM:13 o 14):'))
        print('RESULTADO: El area es ',((numero7+numero6)/2)*numero8)
    
    elif opcion== 25:
        print('')
        numero7=float(input('LADO:'))
        numero8=float(input('Nº DE LADO:'))
        print('RESULTADO: El perimetro es ',numero7*numero8)
    
    elif opcion== 26:
        print('')
        numero7=float(input('RADIO:'))
        print('RESULTADO: El perimetro es ',numero7*3.141)
    
    elif opcion== 27:
        print('')
        numero7=float(input('RADIO:'))
        print('RESULTADO: El area es ',3.141*numero7*numero7)

    
    elif opcion== 28:
        print('')
        numero7=float(input('RADIO:'))
        numero8=float(input('ALTURA:'))
        print('RESULTADO: El area es ',2*3.141*(numero7+numero8))
    
    elif opcion== 29:
        print('')
        numero7=float(input('RADIO:'))
        numero8=float(input('ALTURA:'))
        print('RESULTADO: El volumen es ',3.141*(numero7*2)*numero8)
    
    elif opcion== 30:
        print('')
        numero7=float(input('RADIO:'))
        print('RESULTADO: El area es ',4*3.141*(numero7*2))
    
    elif opcion== 31:
        print('')
        numero7=float(input('RADIO:'))
        print('RESULTADO: El volumen es ',(1.3)*3.141*(numero7*+3))

    elif opcion == 32 :
        print('')
        numero7=float(input('ALTURA:'))
        numero8=float(input('RADIO:'))
        numero9=float(input('HIPOTENUSA(si no la sabes debes hacer pitagoras NUM:13 o 14):'))
        print('RESULTADO: El area es ',3.141*(numero8*numero8)+3.141*numero8*numero9,)

    elif opcion == 33 :
        print('')
        numero7=float(input('ALTURA:'))
        numero8=float(input('RADIO:'))
        print('RESULTADO: El volumen es ',(3.141*(numero8*numero8)*numero7)/3,)
    
    elif opcion == 34 :
        print('')
        numero7=float(input('LADO:'))
        print('RESULTADO: El area es ',6*numero7,)

    elif opcion == 35 :
        print('')
        numero7=float(input('LADO:'))
        print('RESULTADO: El volumen es ',(numero7*numero7)*numero7,)
    
    elif opcion == 36:
        print('')


    else:
        print("Opción incorrecta !!! Prueba una variable DISTINTA")
