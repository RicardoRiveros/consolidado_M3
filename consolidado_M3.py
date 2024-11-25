magos = ['Harry Houdini', 'David Blane', 'Teller']
cientificos = ['Newton', 'Hawking', 'Einstein']
otros = ['Messi', 'Pele', 'Juanes']

def hacer_grandioso(magos):
    for i in range(len(magos)):
        magos[i]= "El gran " + magos[i]

def imprimir_nombre(lista):
    for i in lista:
        print(i)

print(magos)
hacer_grandioso(magos)
print("Magos:")
imprimir_nombre(magos)
print("Cientificos:")
imprimir_nombre(cientificos)
print("Otros")
imprimir_nombre(otros)