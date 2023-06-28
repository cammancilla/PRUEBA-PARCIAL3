import numpy as np
import random

nif=[]
nombre=[]
edad=[]


def menu():
    print("1: Grabar datos")
    print("2: Buscar datos")
    print("3: Imprimir certificado")
    print("4: Salir")

a=0
b=0
i=0
verficador=True
verificador2=True

bandera_menu=True

while (bandera_menu==True):
    menu()
    opcion_m= int(input("INGRESE LA OPCIÓN QUE DESEA: "))
        
    if opcion_m==1:
       nif.append(input("Ingrese su NIF: "))

       while verficador==True:
          nombre.append(input("Ingrese su nombre: "))
          if(len(nombre[a])>7):
             verficador=False
          else:
             print("¡El nombre debe de ser de 8 caracteres por lo menos!")  

       while verificador2==True:
          edad.append(int(input("Ingrese su edad: ")))
          if (edad[a]>0):
             verificador2=False
          else:
             print("¡La edad debe ser mayor o igual a 0!") 

       a+1       
        
    if opcion_m==2:
       buscar=input("INGRESE EL NIF QUE DESEA BUSCAR: ")
       for i in nif:
          if i==buscar:
             print("NIF PERSONA: ", nif[b])
             print("NOMBRE: ", nombre[b]) 
             print("EDAD", edad[b])       
             if(len(nif[b])>10):
                print("LA PERSONA PERTENECE A LA UNION EUROPEA")
             else:
                print("La PERSONA NO PERTENCE A LA UNION EUROPEA") 

          else:
             print(" No se encuentra registro de la persona")
             b=+1
             break
          
   
       

    if opcion_m==3:
       certificados = ["Certificado de nacimiento", "Estado conyugal", "Pertenencia a la Union Europea"]
       certificado = random.choice(certificados)
       for i in range (len(nif)):
          certificado=random.choice (certificados)
          print("Certificado: ", certificado) 
          print("NIF: ", nif[i])
          print("NOMBRE: ", nombre[i]) 
          print("EDAD", edad[i])         
          print("-----------------------------------")    


    if opcion_m==4:
       print("PROGRAMA TOTALMENTE HECHO POR CAMILA MANCILLA , VERSION 1 (porque esta vez me salio a la primera, soy una crack)")
       False   
       


    