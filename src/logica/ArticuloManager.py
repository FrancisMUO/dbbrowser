from src.modelo.modelo import Articulo, Comentario
from sqlalchemy.exc import SQLAlchemyError

class ArticuloManager:
    def __init__(self, session):
        self.session = session

    def crear_nrc(self, titulo):
        try:
            articulo = Articulo(titulo=titulo)
            self.session.add(articulo)
            self.session.commit()
            return articulo
        except SQLAlchemyError:
            self.session.rollback()
            raise

    def leer_nrc(self, articulo_id):
        try:
            return self.session.query(Articulo).get(articulo_id)
        except SQLAlchemyError:
            self.session.rollback()
            raise

    def actualizar_nrc(self, articulo_id, nuevo_titulo):
        try:
            articulo = self.leer_nrc(articulo_id)
            if articulo:
                articulo.titulo = nuevo_titulo
                self.session.commit()
            return articulo
        except SQLAlchemyError:
            self.session.rollback()
            raise

    def eliminar_nrc(self, articulo_id):
        try:
            articulo = self.leer_nrc(articulo_id)
            if articulo:
                self.session.delete(articulo)
                self.session.commit()
            return articulo
        except SQLAlchemyError:
            self.session.rollback()
            raise

    def agregar_comentario(self, articulo_id, comentario_texto):
        try:
            articulo = self.leer_nrc(articulo_id)
            if articulo:
                comentario = Comentario(comentario=comentario_texto, articulo=articulo)
                self.session.add(comentario)
                self.session.commit()
                return comentario
            return None
        except SQLAlchemyError:
            self.session.rollback()
            raise

    def leer_comentarios(self, articulo_id):
        try:
            articulo = self.leer_nrc(articulo_id)
            return articulo.comentarios if articulo else []
        except SQLAlchemyError:
            self.session.rollback()
            raise
