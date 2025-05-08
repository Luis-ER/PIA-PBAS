import requests
perros = []

def obtener_foto(fin):
    for i in range (0,fin, 1):
        url = "https://dog.ceo/api/breeds/image/random"
        try:
            datos = requests.get(url)
            datos.raise_for_status()
            pagina = datos.json()
            datos2 = requests.get(pagina["message"])
            datos2.raise_for_status()
            for clave, valor in pagina.items():
                print(clave, "-" ,valor)
            aux = guardar_foto(pagina["message"])
            perros.append(aux)
        except requests.exceptions.HTTPError:
            print(f"Error: La página no fue encontrada.")
        except requests.exceptions.ConnectionError:
            print(f"Error: No se pudo conectar a la API. Verifica tu conexión.")
        except requests.exceptions.Timeout:
            print(f"Error: La solicitud tardó demasiado en responder.")
        except ValueError:
            print(f"Error: No se pudieron procesar los datos.")

def guardar_foto(mensaje):
    lista_aux = []
    text = mensaje.replace("https://images.dog.ceo/breeds/", "")
    lista_aux2 = text.split("/")
    traslado = {
        "raza" : lista_aux2[0],
        "imagen" : lista_aux2[1]}
    lista_aux.append(traslado)
    return lista_aux

while True:
    try:
        fin = int(input("Número de fotos: "))
        if 0 > fin:
            raise ValueError("Rango inválido")
        break
    except ValueError as e:
        print(f"Error en la entrada {e}. Inténtalo de nuevo.")

obtener_foto(fin)
print(perros)


fo=open("Caninos.txt","w")
info=str(perros)
fo.write(info)
fo.close()

fo=open("Caninos.txt","r")
print(fo.read())
fo.close()
