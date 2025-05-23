from src.modelo.declarative_base import Session, Base, engine
from src.logica.ArticuloManager import ArticuloManager

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Configurar una nueva sesión para cada prueba
session = Session()
manager = ArticuloManager(session)

# crear articulos
articulo1 = manager.crear_nrc("Alumnos")
articulo2 = manager.crear_nrc("Cursos")
articulo3 = manager.crear_nrc("Aulas")

# crear comentarios
manager.agregar_comentario(articulo1.id, "Identificador Alumnos")
manager.agregar_comentario(articulo2.id, "Identificados de Cursos")
manager.agregar_comentario(articulo3.id, "Identificador de Aulas")
