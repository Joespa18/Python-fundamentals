'''
1. Cuenta regresiva: crea una función que acepte un número como entrada. Devuelve una lista nueva que cuente de uno en uno, desde el número (como elemento 0) hasta 0 (como último elemento). 
Ejemplo: countdown(5) debería devolver [5,4,3,2,1,0]
'''
def cuentaRegresiva(numero):
    x = []
    for i in range(numero, -1, -1):
        x = i
        print(x)
cuentaRegresiva(5)

'''
2. Imprimir y devolver: crea una función que reciba una lista con dos números. Imprime el primer valor y devuelve el segundo.
Ejemplo: imprimir_y_devolver([1,2]) debe imprimir 1 y devolver 2
'''
a = 1
b = 2
c = [a,b]
def imprimir_y_devolver(c):
    print(a)
    return b
imprimir_y_devolver(c)

'''
3. Primero más longitud: crea una función que acepte una lista y devuelva la suma del primer valor de la lista, más la longitud de la lista.
Ejemplo: primero_mas_longitud([1,2,3,4,5]) debe devolver 6 (primer valor: 1 +length: 5)
'''
x = []
def primero_mas_longitud(x):
    suma = x[0] + len(x)
    # print(suma)
    return suma
primero_mas_longitud([1,2,3,4,5])

'''
4. Valores mayores que el segundo: escribe una función que acepte una lista y cree una nueva que contenga solo los valores de la lista original que sean mayores que su segundo valor. Imprime cuántos valores son y luego devuelve la lista nueva. Si la lista tiene menos de 2 elementos, has que la función devuelva False
Ejemplo: valores_mayores_que_el_segundo([5,2,3,2,1,4]) debe imprimir 3 y devolver [5,3,4]
Ejemplo: valores_mayores_que_el_segundo([3]) debe devolver False
'''
x = []
def valores_mayores_que_el_segundo(x):
    if len(x)<2:
        print("false")
        return
    y = []
    for i in range(0, len(x), +1):
        if x[i]>x[1]:
            y += [x[i]]
    print(len(y))
    return(y)
valores_mayores_que_el_segundo([5,2,3,2,1,4])

'''
5. Esta longitud, ese valor: escribe una función que acepte dos enteros como parámetros: tamaño y valor. La función debe crear y devolver una lista cuya longitud sea igual al tamaño dado, y cuyos valores sean todos el valor dado.
Ejemplo: length_and_value(4,7) debe devolver [7,7,7,7]
Ejemplo: length_and_value(6,2) debe devolver [2,2,2,2,2,2]
'''
def longitud_y_valor(longitud,valor):
    salida = []
    for i in range (0,longitud):
        salida.append(valor)
    return salida

print(longitud_y_valor(4,7))
print(longitud_y_valor(6,2))