#Importacion de librerias a utilizar
import matplotlib.pyplot as plt 
import numpy as np
from math import sin, cos, radians,sqrt
import keyboard #se puede cerrar el programa con esta paqueteria pero se tiene que instalar con pip install keyboard por lo cual usamos msvcrt
import msvcrt # esta libreria no necesita ser instalada para usarse en windows
import tools3d 

#Carlos Yolatl Joshua Montero Cortez 
#N° Control: 18390044
#Maestro: May Canché Isaias
#Materia: Graficación
"""En el siguiente codigo se va a calcular el area de 3 triangulos para poder saber si el Hitpoint (el punto 
que el usuario ingrese) esta adentro del area de estos 3 triangulos, usaremos la formula de Heron 
para determinar el area de dichos triangulos.

Tenemos 3 triangulos; el triangulo base, va de los puntos 0,1 y 2 = A
de ahi sale el segundo el cual va de los puntos 0, 1 y 3 = A1 y por ultimo el tercer 
triangulo que va de los puntos 0, 3 y 2 = A2 

Para saber si el punto proporcionado esta dentro o fuera debemos 
calcular las areas de estos triangulos por lo que:
si LA SUMA DEL A1 + A2 > A, el hitpoint esta afuera de los limites y  
si LA SUMA DEL A1 + A2 < A, el hitpoint esta dentro de los limites. 
"""



while True:
    
    plt.axis([0,150,100,0]) #Declaramos el area donde se mostra el tamaño de la ventana
    plt.title('Calcular el Area de los triagulos con formula de Heron')#se escrite el titulo  del programa
    plt.ylabel('Y') #Se inserta el eje Y 
    plt.xlabel('X') #Se inserta el eje  X 
    plt.axis('on')
    plt.grid(True)

    
    #Se piden y se asigna los valores del Hitpoint, los cuales el usuario solicita
    xhit=float(input('Insertar Valor del hitpoint en x'))
    yhit=float(input('Insertar Valor del hitpoint en y'))
    #Se asignas las coordenadas de los puntos para crear los triangulos
    x=[40,30,80,xhit] 
    y=[60,10,60,yhit]
    z=[0,0,0,0]
    #Son los puntos que definen las lineas del triangulo base en el plano
    plt.plot([x[0],x[1]],[y[0],y[1]],color='k') 
    plt.plot([x[1],x[2]],[y[1],y[2]],color='k')
    plt.plot([x[2],x[0]],[y[2],y[0]],color='k')
    plt.scatter(x[3],y[3],s=20,color='r')
    #Se trazan los lados para los triangulos de las lineas punteadas
    plt.plot([x[0],x[3]],[y[0],y[3]],linestyle=':',color='b') 
    plt.plot([x[1],x[3]],[y[1],y[3]],linestyle=':',color='g')
    plt.plot([x[2],x[3]],[y[2],y[3]],linestyle=':',color='r')
    #Se insertan las etiquetas de las esquinas del triangulo (0,1,2,3)
    plt.text(35,63,'0') 
    plt.text(25,10,'1')
    plt.text(83,63,'2')
    plt.text(x[3]+2,y[3],'3')
    #Calculamos las dimensiones del triangulo base 
    #Va del punto 0 al 1
    a=x[1]-x[0] 
    b=y[1]-y[0]
    c=z[1]-z[0]
    Q01=sqrt(a*a+b*b+c*c)
    #Va del punto 2 al 1
    a=x[2]-x[1]
    b=y[2]-y[1]
    c=z[2]-z[1]
    Q12=sqrt(a*a+b*b+c*c)
    #Va del punto 2 al 0
    a=x[2]-x[0]
    b=y[2]-y[0]
    c=z[2]-z[0]
    Q02=sqrt(a*a+b*b+c*c)
    #Este es el calculo para trazar las distancias de las lineas punteadas que hacen los otros 2 triangulos
    #Va del punton 1 al 3
    a=x[1]-x[3]
    b=y[1]-y[3]
    c=z[1]=z[3]
    Q13=sqrt(a*a+b*b+c*c)
    #Va del punto 2 al 3
    a=x[2]-x[3]
    b=y[2]-y[3]
    c=z[2]-z[3]
    Q23=sqrt(a*a+b*b+c*c)
    #Va del punto 0 al 3
    a=x[0]-x[3]
    b=y[0]-y[3]
    c=z[0]-z[3]
    Q03=sqrt(a*a+b*b+c*c)
    #Calculo de areas y aplicacion de la formula de HERON Formula de Heron: 
    # S=(a+b+c)/2 
    # A=√s(s-a)(s-b)(s-c)
    s=(Q01+Q12+Q02)/2 
    A=sqrt(s*(s-Q01)*(s-Q12)*(s-Q02))
    s1=(Q01+Q03+Q13)/2
    A1=sqrt(s1*(s1-Q01)*(s1-Q03)*(s1-Q13))

    s2=(Q02+Q23+Q03)/2
    A2=sqrt(s2*(s2-Q02 )*(s2-Q23)*(s2-Q03))
        #Se inserta la etiqueta del Area: A
        #Se muestra los datos que tiene el area A
    plt.arrow(70,55,10,15,linewidth=.5,color='grey')#Flecha que indica el area Del triangulo base: A
    plt.text(82,73,'A',color='k')
    plt.text(100,40,'A=') 
    dle='%7.0f'% (A)
    dls=str(dle)
    plt.text(105,40,dls)
    #Se inserta la etiqueta del Area: A1
    #Se muestra los datos que tiene el area A1
    plt.text(100,45,'A1=',color='r')
    dle='%7.0f'% (A1)
    dls=str(dle)
    #Se inserta la etiqueta del Area: A2
        #Se muestra los datos que tiene el area A2
    plt.text(105,45,dls)
    plt.text(100,50,'A2=',color='g')
    dle='%7.0f'% (A2)
    dls=str(dle)
    #Se inserta la etiqueta del Area: A1 + A2
    #Se muestra los datos que  resulta de las areas A1 + A2
    plt.text(105,50,dls)
    plt.text(91,55,'A1+A2=',color='b')
    dle='%7.0f'% (A1+A2)
    dls=str(dle)
    plt.text(105,55,dls)
    
    #Verificamos si la suma del Area A1 + A2 es mayor a el area A, de ser cierto te muestra que el el hitpoint esta fuera del Area de los triangulos
    #Caso contrario te dice que esta dentro del area de los triangulos
    if A1+A2 > A:
        plt.text(30,83,'El Hitpoint esta fuera del area de los triangulos')    
    else:
        plt.text(30,83,'El Hitpoint esta dentro del area de los triangulos')

    
    #Se muestra el programa 
    plt.show()

    #Se determina si se preciono una tecla, encaso de ser la tecla ESC detiene el codigo, caso contrario continua el codigo
    print('Precione la tecla ESC para finalizar el programa')
    decision=msvcrt.getch() 
    if decision == chr(27).encode():
        break
