from multidict import MultiDict

# Crear un MultiDict
hashmap = MultiDict()

# Agregar múltiples valores para la misma clave
hashmap.add("C", "10uf")
hashmap.add("C", "22uf")
hashmap.add("R", "3ohm")

# Obtener todos los valores para "clave1"
valores_para_clave1 = hashmap.getall("C")
print(valores_para_clave1)


# Define an array of dimension 2
dim= [[] for _ in range(2)]

dim[0].append(1)
dim[1].append(7)



