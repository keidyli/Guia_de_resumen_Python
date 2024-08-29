#Contenido de Arrays:

# 1) Lista: Estructura de datos que se utiliza para almacenar en secuencia.
#Contiene muchos tipos de datos.
#Las listas son mutables pueden cambiar sus valores.

#Ejemplos: 

my_List= [1, 3, 56, 7] 
print(my_List)

#Metodo que agrega un elemento al final.
my_List.append (8) 
print(my_List)

#Insertar un elemento en un indice especifico. 
my_List.insert(0, 6) 
print (my_List)

#Otra manera de insertar
position= 6
my_List.insert(position, 46)
print(my_List)

#Elimina un elemento de primer lugar (si se repite).
my_List.remove(7)  

#Verificando si existe un elemento en la lista.
if (1 in my_List):
    print("true")
else:
    print("no se encuentra")


#Cambiar y actualizar el valor por indice:
my_List [1]= 76 
print(my_List)


#Metodos de las listas.
# (.pop) elimina y returna un valor de la lista.
# (.reverse) pone el orden al reves.
# (.extend) entiende el array agregandole mas elementos. 
# (.count) contar cuentas veces se repite en el arrays.
# (.sort) ordena el array ascendente o descendente.
# (.index) indica cual es el indice de un elemento.

#Metodo que imprime el tamaño de la Lista.
print(len(my_List)) 


#  Tuplas: 
# estructura de datos inmutable que contiene elementos secuenciale ordenados.
# Valores variados. No se pueden cambiar los valores. Protege la data 

#Ejemplos:

my_Tuple= (1, 8, 52, 5)
print(my_Tuple[2])
print(my_Tuple.index(1))


# Diccionarios: Es una coleccion de elementos ordenados por pares ("clave": valor).

edad={"shaila": 17, "mikaela": 34}
print(edad["shaila"])

#Actualiza el valor.
edad["mikaela"]= 78 
print(edad)

# Metodo que elimina la clave con su valor.
del edad["mikaela"] 
print(edad)

edad ["Lina"]= 180  #Agregar un nuevo clave-valor.
print(edad)

#Caracteristicas:
#Las claves deben ser unicas e inmutables.
#Los valores pueden ser de cualquier tipo, repetidos y mutables.
#los pares c-v pueden ser modificados, eliminados. 


#  Ciclo FOR:
#Estructura de control que repite lineas de codigo.
#Exclusivos para hacer recorridos y mostrar datos.
#Se usa mucho para recorrer los datos en listas, diccionarios y tuplas. 

for i in range (4):
  print(i)

for ii in "Sendaya":
   print(ii)

#Ejemplo en diccionario: 
tuplee= {"m":2, "n": 3}
for clave in tuplee:
   print(clave)

#Mostrando el los valores del diccionario.
for valor in tuplee.values():
   print(valor)

#Mostrando las claves y los valores del diccionario.
for clavee, valorr in tuplee.items():
   print(clavee, valorr)
