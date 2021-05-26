# Uso de comillas símples y dobles en cadenas de texto

mi_texto = '"Master"'
mi_texto2 = "en \"Python\" "

texto_unido = mi_texto + " " + mi_texto2
print(texto_unido)

#Se admiten caracteres de escape \x

texto_unido = mi_texto + "\n" + mi_texto2
print(texto_unido)

texto_unido = mi_texto + "\t" + mi_texto2
print(texto_unido)