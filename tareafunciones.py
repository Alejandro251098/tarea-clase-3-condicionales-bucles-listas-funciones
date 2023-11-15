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

class cola :
    def tareas_hogar(tareas):
        tareas.elementos= [] 
        
    def agregar_tareas(tareas,elemntos):
        tareas.elementos.append(elemntos)
        
    def eliminar_tarea(tareas ):
         if tareas.elementos  :
             return tareas.elementos.pop(0)
         
         else:
             return("la cola de tareas esta vacia")
cola_tareas=cola()

cola_tareas.agregar_tareas("ir a mercar")
cola_tareas.agregar_tareas("lavar la ropa")
cola_tareas.agregar_tareas("lavar la loza")
cola_tareas.agregar_tareas("barrer y trapear")

print(cola_tareas)         
              
# ejercicio 7 : contar elementos unicos