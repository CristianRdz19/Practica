#FUNCION 1

def intercambiar(txt):
    txt_cambiado = ""

    #i = letra por letra.
    
    for i in txt:
        if i == i.upper():
            txt_cambiado = (txt_cambiado + i.lower())
        elif i == i.lower():
            txt_cambiado = (txt_cambiado + i.upper())
    return txt_cambiado

texto = input("Ingrese un texto: ")
txt_cambiado = intercambiar(texto)
print("Texto cambiado: ",txt_cambiado)