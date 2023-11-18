# EJERCICIO 2 :verificar paridad

# def verificar_pares(numero):
#     if (numero % 2) == 0: 
#         print('Es par')
#     else:
#         print('Es impar')

# verificar_pares(3) 


# EJERCICIO 3 : DICCIONARIO DE ESTUDIANTES 


# estudiantes = {}

# def agregar(estudiante,nombre,edad, calificacion):

#     estudiante[nombre] = {
#         "edad":edad , 
#         "calificacion":calificacion
#     }        


#     print(estudiante)


# agregar(estudiantes,"alejandro" , 25 , 4.5)
# agregar(estudiantes,"juan" , 22 , 4)
# agregar(estudiantes,"camila" , 21 , 5)      

# def elimina(estudiante, nombre):
#     if nombre in estudiante:
#         del estudiante[nombre]
#         print("estudiante esliminado")
#     else:
#         print("no se encontro el estudiante")     
#     print(estudiante)        

# elimina(estudiantes , "juan")       


# EJERCICIO 4 : INVERTIR LISTA 



# def invertir_lista (lista) :
#     lista.reverse()
#     return lista


# lista = [ "alejandro" , 25 , "camila" , 22 , "manolo" , 7 ,"sussy" , 4]
# print(invertir_lista(lista))
  
  
#  EJERCICIO 5 : VALIDACION DE PARENTESIS 

# def validar_parentesis(parentesis) :
#     validar =[] 
#     caracteres = { "(" : ")", "[" :"]" , "{":"}"}   
    
#     for c in parentesis :
#         if c in caracteres :
#             validar.append(c)
      
#         elif  len(caracteres) == 0 or c != caracteres[validar.pop()] :
#               return False
          
          
#     return len(validar) == 0

# print(validar_parentesis("([{}])"))
# print(validar_parentesis("(((())))"))
# print(validar_parentesis("()[]{}("))        


# EJERCICIO 6 = cola de tareas


# def agregar(tareas):
    
#     if tareas not in lista_tareas:
#         lista_tareas.append(tareas)
        
# def eliminar(tareas):
#     if tareas in lista_tareas:
#         lista_tareas.remove(tareas)
                
# lista_tareas = []

# agregar("comprar comida")
# agregar("lavar la ropa")
# agregar("lavar la loza")
# agregar("estudiar y terminar trabajos")
    
    
# for tareas in lista_tareas :
#     print(tareas)
    
    
# eliminar("comprar comida")

# print("la nueva lista es:") 
# for tareas in lista_tareas:
#     print( tareas)     



              
# ejercicio 7 : contar elementos unicos


# def elemntos_unicos(lista):
#     elemntos_unicos = set(lista)
#     return len(elemntos_unicos)

# lista = [1 ,2 ,3 ,4 ,5 ,1 ,2 ,3 ,4 ,5,1 ,2 ,3 , 4 ,5 ]
# print(elemntos_unicos(lista))

# EJERCICIO 8 : COMPROBACION DE PALINDROMOS


# def es_palindromo (texto):
#     texto=texto.lower()
#     texto_sin_espacio = texto.replace(" ","")
#     return texto_sin_espacio == texto_sin_espacio[:: -1]         
# print(es_palindromo("luz azul"))
# print(es_palindromo("palabra"))


# EJERCICIO 9 : pila historial de navegacion


  
# def agregar_pagina(paginas):
#     if paginas not in historial:
#        historial.append(paginas)

# def eliminar_pagina(paginas):
#     if paginas in historial:
#         historial.pop()
        

# def retroceder_pagina(historial):
#     pagina_anterior = historial.pop()
#     print(f"retrocede a la pagina{pagina_anterior}")
    
            
                
# historial = []

# agregar_pagina("www.facebook.com")
# agregar_pagina("www.youtube.com")
# agregar_pagina("www.google.com")
# agregar_pagina("www.chatgpt.com")    
# for paginas in historial:
#     print(paginas)
    
# eliminar_pagina("www.google.com")
# print("el historial de navegacion es ")
# for paginas in historial:
#     print(paginas)    

# retroceder_pagina(historial)


    
# EJERCICIO 10 : diccionario de frecuencia


# def frecuencia(lista):
#     diccionario = {}
#     for i in  lista :
#         if i in diccionario :
#             diccionario[i] +=1
#         else :
#             diccionario[i] = 1
#     return diccionario

# lista = [ "hola" , "mundo", "mundo", "tarea","tarea", "tarea", "cuatro", "cuatro","cuatro", "cuatro"] 
# print(frecuencia(lista))                


# EJERCICIO 11 :Multiplicacion de matrices


# def multi_matrix (matrix1 ,matrix2) :
#     fil1 = len(matrix1)
#     col1 = len(matrix1[0]) 
    
#     fil2 = len(matrix2)
#     col2 = len(matrix2[0]) 
    
#     if col1 != fil2:
#        print("no se pueden multiplicar las matrices")
#        return
   
#     result = [[0 for col1 in range(col2)] for row in range(fil1)]
    
#     for i in range(fil1):
#         for j in range(col2):
#             for k in range(col1):
#                 result[i][j] += matrix1[i][k] * matrix2[k][j]
                
#     return result

# matrix1=[[1,2],[3,4]]
# matrix2=[[5,6],[7,8]]

# result = multi_matrix(matrix1,matrix2)

# print(result)      

# EJERCICIO 12: ORDENAR UNA LISTA DE PALABRAS


# def ordenar_lista(lista):
#     return lista.sort()

# lista =["bala","elefante","ala","casa","dedo","gato" ,"fuego"]

# ordenar_lista(lista)
# print(lista)


# EJERCICIO 13 : VERIFICACION NUMEROS PRIMOS

# def verificar_primos(numero):
#     contador = 0
#     if numero < 1 :
#       return print("ingrese un numero mayor a 1")
#     for i in range(1, numero +1 ):
#      if (numero % i) == 0: 
#         contador+=1
        
    
        
# numero=int(input("ingrese un numero"))

# verificar_primos(numero)
# print("es un numero primo")


# EJERCICIO 14 :CALCULADORA OPERACIONES BASICAS

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    else:
        return a / b
    
a = 5
b = 10

resultado_suma =  sumar(a,b)  
resultado_resta = restar(a,b)
resultado_multiplicacion=multiplicar (a,b)
resultado_dividir=dividir(a,b)

print(f"la suma de: {a}+{b} = {resultado_suma}")

# EJERCICIO 15 : CONVERSION DE UNIDADES

# def celcios_to_fahrenheit(celcios):
#     return (celcios * 9/5) + 32

# def fahrenheit_to_celcios(fahrenheit):
#     return (fahrenheit - 32) * 5/9

# def km_to_millas(km):
#     return km * 0.621371

# def millas_to_km(millas):
#     return millas * 1.60934


# print(celcios_to_fahrenheit(30)) 
# print(fahrenheit_to_celcios(90)) 
# print(km_to_millas(10))            
# print(millas_to_km(5)) 
