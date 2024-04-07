from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi_erp.database import get_db, set_fields_from_dict
from fastapi_erp.model.api.item import ItemCreate
from fastapi_erp.model.base.item import Item
from fastapi_erp.model.base.user import User

class ItemService:
    
    @staticmethod
    def instance(db: Session = Depends(get_db)) -> 'ItemService':
        return ItemService(db)

    def __init__(self, db: Session):
        self.db = db

    async def get(self, item_id: int):
        return self.db.query(Item).filter(Item.id == item_id).first()

    def list(self, skip: int = 0, limit: int = 100):
        return self.db.query(Item).offset(skip).limit(limit).all()

    def create(self, item: ItemCreate):
        item = Item(**item.dict())
        self.db.persist(item)
        return item.dict()

    async def update(self, item_id: int, new_item: dict):
        item: Item = await self.get(item_id)
        set_fields_from_dict(item, new_item)
        self.db.merge(item)
        return item.dict()
    
    async def delete(self, item_id: int):
        item: Item = await self.get(item_id)
        if item:
            self.db.delete(item)
            return True
        else:
            return False
