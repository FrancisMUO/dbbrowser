from src.modelo.declarative_base import Session, Base, engine
from src.modelo.modelo import Articulo, Comentario

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Configurar una nueva sesión para cada prueba
session = Session()

# crear articulos
articulo1 = Articulo(titulo="Código Espinoza")
session.add(articulo1)
session.commit()

articulo2 = Articulo(titulo="El futuro de Python")
session.add(articulo2)
session.commit()

# crea comentarios

comentario = Comentario(comentario="Tiene blogs de Python", articulo_id=articulo1.id )
session.add(comentario)
session.commit()

comentario = Comentario(comentario="Es util para IA", articulo_id=articulo2.id )
session.add(comentario)
session.commit()

comentario = Comentario(comentario="ES fácil crear SPA", articulo_id=articulo2.id )
session.add(comentario)
session.commit()

