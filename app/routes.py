from fastapi import APIRouter, HTTPException
from .models import items

router = APIRouter()

@router.get("/items")
def get_items():
    return items

@router.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@router.post("/items")
def add_item(payload: dict):
    new_id = len(items) + 1
    payload["id"] = new_id
    items.append(payload)
    return payload
