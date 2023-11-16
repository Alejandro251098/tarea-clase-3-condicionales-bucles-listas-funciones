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


def es_palindromo (texto):
    texto=texto.lower()
    texto_sin_espacio = texto.replace(" ","")
    return texto_sin_espacio == texto_sin_espacio[:: -1]         
print(es_palindromo("luz azul"))
print(es_palindromo("palabra"))