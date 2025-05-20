import requests, re
perros = []
lista_razas = []
warning = "\nEl código lleva 10 intentos. ¿Desea continuar?\nSí = cualquier tecla\nNo = 1\n"

def obtener_foto(det, flag = True):
    i = 0
    j = 1
    while flag:
        url = "https://dog.ceo/api/breeds/image/random"
        try:
            datos = requests.get(url)
            datos.raise_for_status()
            pagina = datos.json()
            datos2 = requests.get(pagina["message"])
            datos2.raise_for_status()
            for clave, valor in pagina.items():
                print(clave, "-" ,valor)
            aux, flag = guardar_foto(pagina["message"], det)
            perros.append(aux)
            i += 1
            if i == 10:
                continuar = input(warning)
                if continuar == "1":
                    flag = False
                else:
                    i = 0
                    j += 1
        except requests.exceptions.HTTPError:
            print(f"Error: La página no fue encontrada.")
        except requests.exceptions.ConnectionError:
            print(f"Error: No se pudo conectar a la API. Verifica tu conexión.")
        except requests.exceptions.Timeout:
            print(f"Error: La solicitud tardó demasiado en responder.")
        except ValueError:
            print(f"Error: No se pudieron procesar los datos.")

    return j

def guardar_foto(mensaje, det):
    lista_aux = []    
    text = mensaje.replace("https://images.dog.ceo/breeds/", "")
    regex1 = r'^(.+)/[^/]+.jpg'
    traslado1 = re.findall(regex1,text)
    regex2 = r'[^/]+.jpg'
    traslado2 = re.findall(regex2,text)
    lista_aux.append(traslado1)
    lista_aux.append(traslado2)
    repetido = repeticion(traslado1, det)
    return lista_aux, repetido

def repeticion(raza, det):
    flag = True
    lista_razas.append(raza)
    if det != 0:
        cont = lista_razas.count(det)
    elif det == 1:
        det = lista_razas[0]
        cont = lista_razas.count(det)
    else:
        for i in lista_razas:
            cont = lista_razas.count(i)
    if cont > 1:
         flag = False
    return flag


menu = """----REPETICIONES DE RAZAS EN DOG-API----

1. Pomerania
2. Husky
3. Pastor Alemán
4. Al azar
5. Primera raza en repetirse
6. Salir

Elija una opción: """

while True:
    try:
        opc = int(input(menu))
        if opc == 1:
            det = "pomeranian"
            break
        elif opc == 2:
            det = "husky"
            break
        elif opc == 3:
            det = "germanshepherd"
            break
        elif opc == 4:
            det = 1
            break
        elif opc == 5:
            det = 0
            break
        elif opc == 6:
            print("Cerrando programa")
            exit()
            break
        else:
            print(f"Error en {opc}. Intente de nuevo.")
    
    except ValueError as e:
        print(f"Error en la entrada {e}. Inténtalo de nuevo.")

precaucion = obtener_foto(det)
if precaucion > 3:
    input("El código se cerrará sin guardar los datos como forma de precaucion")
    exit()
print(perros)
print(lista_razas)

fo = open("Caninos.txt","w")
for i in range(0, len(perros), 1):
    for info in perros[i]:
        conjunto = str(info)
        conjunto = conjunto.strip("['']")
        fo.write(conjunto)
        fo.write("\n")
fo.close()
