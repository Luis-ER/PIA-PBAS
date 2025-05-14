import numpy, statistics, collections, re
import matplotlib.pyplot as plt

i = 0
razas = []
contador = []

with open ("Caninos.txt", "r") as archivaldo:
    for linea in archivaldo:
        if i%2 == 0:
            print("Raza")
            razas.append(linea.rstrip("\n"))
        else:
            print("Foto")
        print(linea)
        i += 1

        
try:
    for i in range(len(razas)):
        cont = 1
        x = razas[i]
        for j in range(i + 1, len(razas), 1):
            if x == razas[j]:
                cont += 1
                razas.pop(i)
        contador.append(cont)

except IndexError:
    print("Elemento borrado de la lista")



print(razas)
print(contador)
x=numpy.array(razas)
y=numpy.array(contador)
plt.scatter(x,y)
plt.colorbar()
plt.title("Razas vs Cantidad")
plt.xlabel("Razas")
plt.ylabel("Cantidad")
plt.show()

media=statistics.mean(contador)
mediana=statistics.median(contador)
moda=statistics.mode(contador)
desviacionestandar=statistics.pstdev(contador)
distribucion=statistics.pvariance(contador)

print(media)
print(mediana)
print(moda)
print(desviacionestandar)
print(distribucion)
