import datetime

class Libro:
    def __init__(self, titulo, autor, paginas):
        if not isinstance(titulo, str) or not isinstance(autor, str) or not isinstance(paginas, int):
            raise ValueError("Los tipos de datos de los atributos son incorrectos")
        if not titulo or not autor or paginas <= 0:
            raise ValueError("Los atributos no pueden ser nulos o vacíos, y el número de páginas debe ser mayor que 0")

        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.fecha_publicacion = datetime.date.today()

    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

    def get_paginas(self):
        return self.paginas

    def get_fecha_publicacion(self):
        return self.fecha_publicacion

    def set_titulo(self, titulo):
        if not isinstance(titulo, str) or not titulo:
            raise ValueError("El título no puede ser nulo o vacío")
        self.titulo = titulo

    def __str__(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}\nPáginas: {self.paginas}\nFecha de Publicación: {self.fecha_publicacion}"

    def __eq__(self, other):
        if isinstance(other, Libro):
            return (
                self.titulo == other.titulo and
                self.autor == other.autor and
                self.paginas == other.paginas and
                self.fecha_publicacion == other.fecha_publicacion
            )
        return False
