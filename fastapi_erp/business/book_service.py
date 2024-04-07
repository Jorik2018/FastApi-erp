from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi_erp.database import get_db
from fastapi_erp.model.api.book import BookSchema
from fastapi_erp.model.base.book import Book

class BookService:
    
    @staticmethod
    def instance(db: Session = Depends(get_db)) -> 'BookService':
        return BookService(db)

    def __init__(self, db: Session):
        self.db = db

    def list(self, skip: int = 0, limit: int = 100):
        return self.db.query(Book).offset(skip).limit(limit).all()

    def create(self, book: BookSchema):
        return Book()