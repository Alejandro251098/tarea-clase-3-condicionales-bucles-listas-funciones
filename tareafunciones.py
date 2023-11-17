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


# cola_tareas = [ "hacer mercado" , "lavar loza" , "hacer el aseo" ]

# def agregar_tarea(tareas_pendientes):
#     tareas_pendientes.insert(cola_tareas)
    
#     print(cola_tareas)
# agregar_tarea("lavar la ropa")
# agregar_tarea("terminar las tareas de la U")
# agregar_tarea("pasear el perro")


# def eliminar_tareas(tareas_pendientes , cola_tareas):
    
#     if tareas_pendientes in cola_tareas:
#        cola_tareas.pop(0)
       
#     else :
#        print("tareas no encontrada o lista vacia ")
# print(cola_tareas)
    
           
# eliminar_tareas(cola_tareas)

              
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


# historial = []


# def agregar(paginas):
    
#     historial = paginas.append()
#     pagina_actual = historial
#     if pagina_actual in historial.pop( -1):
#         print(pagina_actual)
    
# agregar("www.youtube.com")
# agregar("www.facebook.com")
# agregar("www.goolge.com")         
    

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

# def calculadora():


# EJERCICIO 15 : CONVERSION DE UNIDADES

def celcios_to_fahrenheit(celcios):
    return (celcios * 9/5) + 32

def fahrenheit_to_celcios(fahrenheit):
    return (fahrenheit - 32) * 5/9

def km_to_millas(km):
    return km * 0.621371

def millas_to_km(millas):
    return millas * 1.60934


print(celcios_to_fahrenheit(30)) 
print(fahrenheit_to_celcios(90)) 
print(km_to_millas(10))            
print(millas_to_km(5)) 
