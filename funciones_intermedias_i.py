'''
1.Actualizar valores en diccionarios y listas
'''
x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1.Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(x)

# 2.Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
estudiantes[0]['last_name'] = 'Bryant'
print(estudiantes[0])

# 3.En el directorio_deportes, cambia "Messi" por "Andrés".
directorio_deportes['fútbol'][0] = 'Andrés'
print(directorio_deportes)
# directorio_deportes.update({'fútbol':['Andrés', 'Ronaldo', 'Rooney']}) #otra forma

# 4.Cambia el valor 20 en z a 30.
z[0]['y'] = 30
print(z)

'''
2. Iterar a través de una lista de diccionarios
'''

estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(cualquier_lista):
    for estudiante in cualquier_lista:
        for clave, valor in estudiante.items():
            print(clave,"-", valor)

iterateDictionary(estudiantes)

# def iterateDictionary(cualquier_lista):    #otra forma
#     for estudiante in cualquier_lista:
#         for clave in estudiante:
#             print(clave, "-", estudiante[clave])

# iterateDictionary(estudiantes)

# def iterateDictionary(some_list):    #otra forma
#         for estudiante in some_list:
#             print(estudiante['first_name'], end=" - ")
#             print(estudiante['last_name'])

# iterateDictionary(estudiantes)

'''
3. Obtener valores de una lista de diccionarios.
Crea una función iterateDictionary2(key_name, some_list) que, dada una lista de diccionarios y un nombre de clave, la función imprima el valor almacenado en esa clave para cada diccionario. Por ejemplo: 

iterateDictionary2('name', estudiantes) debería generar:
Michael
John
Mark
KB
Y iterateDictionary2('last_name', estudiantes) debería generar:
Jordan
Rosales
Guillen
Tonel
'''

def iterateDictionary2(key_name, some_list):
        for estudiante in some_list:
            # for clave in estudiante:
            if key_name =='first_name':
                print(estudiante['first_name'])
            elif key_name == 'last_name':
                print(estudiante['last_name'])
            else:
                print('ingresar un key_name válido')
                return

iterateDictionary2('first_name', estudiantes)

'''
4. Iterar a través de un diccionarios con valores de lista
Crea una función printInfo(some_dict) que, dado un diccionario cuyos valores son todos listas, imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores asociados dentro de la lista de cada clave. Por ejemplo:

dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
# salida:
7 UBICACIONES
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 INSTRUCTORES
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon

'''

dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for clave, valor in dojo.items():
        print("\n",len(valor),clave.upper())
        for x in valor:
            print(x)

printInfo(dojo)

# def printInfo(some_dict):    #otra forma
#     print(len(dojo['ubicaciones']),"UBICACIONES")
#     for ubicacion in dojo['ubicaciones']:
#         print(ubicacion)

#     print("\n")

#     print(len(dojo['instructores']),"INSTRUCTORES")
#     for instructor in dojo['instructores']:
#         print(instructor)

# printInfo(dojo)