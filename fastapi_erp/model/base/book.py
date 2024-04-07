from sqlalchemy import Column, Integer, String
from fastapi_erp.database import Base

class Book(Base):
    # nombre de la tabla
    __tablename__ = "books"
    
    # Las columnas de nuestra tabla y el tipo de dato de cada una
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)