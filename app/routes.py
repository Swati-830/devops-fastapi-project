from fastapi import APIRouter, HTTPException
from models import items

router = APIRouter()

@router.get("/items")
def get_items():
    return items

@router.get("/items/{item_id}")
def get_single_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

