from sqlalchemy.orm import Session
from fastapi_erp.model.api.item import UserCreate
from fastapi_erp.model.base.user import User

class UserService:
    
    @staticmethod
    def create(db: Session, user: UserCreate):
        fake_hashed_password = user.password + "notreallyhashed"
        db_user = User(email=user.email, hashed_password=fake_hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
