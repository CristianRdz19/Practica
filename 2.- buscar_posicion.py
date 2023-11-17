#FUNCION 2

def buscar_posicion(texto, texto_buscado):
    encontrado = False
    for i in range(len(texto) - len(texto_buscado) + 1):
        if texto[i:i+len(texto_buscado)] == texto_buscado:
            print("La cadena fue encontrada en la posicion:", i)
            encontrado = True
            break
    if encontrado == False:
        print("-1")

texto = input("Ingrese un texto: ")
texto_buscado = input("Ingrese el texto a buscar: ")
resul = buscar_posicion(texto, texto_buscado)