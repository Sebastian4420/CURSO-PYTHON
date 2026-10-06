
#creando una lista (se pueden modificar)
lista = ["Lucas Dalto","Soy Dalto",True,1.85, "Soy Dalto"]

#creando una tupla (no pueden modificar)
tupla = ("Lucas Dalto","Soy Dalto",True,1.85, "Soy Dalto")

#esto es vàlido
#lista[3] = "Maquinola"

#esto no
#tupla[3] = "Maquinola"


#creando un conjunto (set) (no se accede a elementos por ìndice, no almacena datos duplicados)
conjunto = {"Lucas Dalto","Soy Dalto",True,1.85, "Soy Dalto"}

#print(conjunto[3]) -> no puede acceder al elemento


#creando un diccionario (dict) (la estructura es key : value y separamos con comas)
diccionario = {
    'nombre' : "Lucas Dalto",
    'canal' : "Soy Dalto",
    'esta_emocionado' : True,
    'altura' : 1.85,
    'dato_duplicado' : "Soy Dalto"
}

print(diccionario['altura'])





lista= ["Hola", "Sebastián", 7.89, True, "JAJA"]
lista[1] = "Salomé"
print(lista[1])


tupla= ("Hola", "Mi edad es: ", 20)
print(tupla[2]) 

nombre, fecha, curso = ("Sebastián Tobar", "11/04/2026", "Curso de pyhton")
print("Hola, mi nombre es", nombre +
      " y hoy estamos", fecha + "y estoy aprendiendo el "+curso)



