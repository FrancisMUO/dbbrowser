import sys
import os

# Add the project root directory to Python path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(project_root)

from src.modelo.declarative_base import init_db, get_session
from src.modelo.modelo import NRC, DetalleNRC
from sqlalchemy.exc import SQLAlchemyError

class NRCManager:
    def __init__(self, session):
        self.session = session

    def crear_nrc(self, codigo, nombre_curso):
        try:
            nrc = NRC(codigo=codigo, nombre_curso=nombre_curso)
            self.session.add(nrc)
            self.session.commit()
            return nrc
        except SQLAlchemyError:
            self.session.rollback()
            raise

    def agregar_detalle(self, nrc_id, aula, horario, cupo):
        try:
            nrc = self.session.query(NRC).get(nrc_id)
            if nrc:
                detalle = DetalleNRC(
                    aula=aula,
                    horario=horario,
                    cupo=cupo,
                    nrc=nrc
                )
                self.session.add(detalle)
                self.session.commit()
                return detalle
            return None
        except SQLAlchemyError:
            self.session.rollback()
            raise

def main():
    # Inicializar la base de datos
    init_db()
    
    # Obtener una nueva sesión
    session = get_session()
    manager = NRCManager(session)
    
    try:
        # Crear registros NRC
        nrc_matematicas = manager.crear_nrc("NRC1001", "Cálculo Diferencial")
        nrc_programacion = manager.crear_nrc("NRC2002", "Programación Orientada a Objetos")
        nrc_bases_datos = manager.crear_nrc("NRC3003", "Bases de Datos")

        # Agregar detalles de cada NRC
        manager.agregar_detalle(
            nrc_matematicas.id, 
            "B-201",
            "Lunes y Miércoles 7:00-9:00",
            30
        )
        manager.agregar_detalle(
            nrc_programacion.id,
            "Lab-A102",
            "Martes y Jueves 10:00-12:00",
            25
        )
        manager.agregar_detalle(
            nrc_bases_datos.id,
            "Lab-B103",
            "Viernes 14:00-18:00",
            20
        )
        
        print("Sistema NRC inicializado exitosamente")
        print("\nCursos disponibles:")
        print(f"- {nrc_matematicas.codigo} - {nrc_matematicas.nombre_curso}")
        print(f"- {nrc_programacion.codigo} - {nrc_programacion.nombre_curso}")
        print(f"- {nrc_bases_datos.codigo} - {nrc_bases_datos.nombre_curso}")
        
    except Exception as e:
        print(f"Error en la inicialización del sistema NRC: {str(e)}")
    finally:
        session.close()

if __name__ == "__main__":
    main()
