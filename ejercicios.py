import os
"""
Ejercicio 1 VIEJO Y PELUDO
x=[1,2,3,4,5]

i = iter(x)

[print (elem) for elem in i]
"""
"""
EJERCICIO 2 VIEJO Y PELUDO

x=[1,2,3,4,5]

i= iter(x)

[print (3**elem) for elem in i]
"""
"""
EJERCICIO 3 VIEJO Y PELUDO
a= list(range(1,5))
b= list(range(5,10))

c=[a1+b1 for a1,b1 in list(zip(a,b))]

print(c)

"""
"""
EJERCICIO 4 VIEJO Y PELUDO
a=list(range(1,5))
b=['a','b','c','d']

c={ a1:b1 for a1,b1 in zip(a,b)}

print(c)
"""

"""
z = open('palabras.txt','w')
print(flush=True)
cadena=input(' por favor ingrese una cadena')
print(flush=True)
print(bool(cadena))
os.system('pause')
while True:
    
    if cadena:
        break
    else:

        cadena=input(' por favor ingrese una cadena\n')
    
    z.write(cadena + ' ')
    
z.close()
print(z)
"""
z = open('palabras.txt','w')


cadena = input("Por favor, ingrese una cadena (o presione Enter para salir)")
print(bool(cadena))

while(cadena):
    if cadena:
        cadena = input('Por favor, ingrese una cadena (o presione Enter para salir):\n')
    else:
        break    
    z.write(cadena + ' ')
   
z.close()

z=open('palabras.txt','r')
z.read()
