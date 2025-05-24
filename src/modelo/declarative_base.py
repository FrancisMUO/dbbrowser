from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Obtener la ruta del directorio actual
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Crear la ruta completa de la base de datos
DB_PATH = os.path.join(BASE_DIR, 'database.sqlite')

# Configurar la base de datos SQLite con la ruta absoluta
engine = create_engine(f'sqlite:///{DB_PATH}', echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base()

# Crear una función para inicializar la base de datos
def init_db():
    Base.metadata.create_all(engine)

# Crear una función para obtener una nueva sesión
def get_session():
    return Session()