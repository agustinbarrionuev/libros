from ejercicios.libros import Libro

# Crear un diccionario de libros donde la clave es una identificación única y el valor es el objeto Libro
libros = {
    1: Libro("El Gran Gatsby", "F. Scott Fitzgerald", 180),
    2: Libro("Don Quijote", "Miguel de Cervantes", 863),
    3: Libro("1984", "George Orwell", 328),
    4: Libro("Cien años de soledad", "Gabriel García Márquez", 417),
    5: Libro("Matar un ruiseñor", "Harper Lee", 324),
    6: Libro("El Gran Gatsby", "F. Scott Fitzgerald", 180),
}

# Mostrar información de los libros
for id, libro in libros.items():
    print(f"Información del libro {id}:")
    print(libro)
    print()

# Comprobar si los libros son iguales o distintos automáticamente
for id1, libro1 in libros.items():
    for id2, libro2 in libros.items():
        if id1 != id2 and libro1 == libro2:
            print(f"Los libros {id1} y {id2} son iguales.")
