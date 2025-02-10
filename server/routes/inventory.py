from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from server.database import SessionLocal, InventoryItem, init_db
from server.schemas import InventoryItemSchema  # Import Pydantic model

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Initialize database on startup
init_db()
@router.get("/inventory")
async def get_inventory(db: Session = Depends(get_db)):
    """
    Fetches all inventory items.
    """
    items = db.query(InventoryItem).all()  # Fetch all inventory items
    return [{"name": item.name, "quantity": item.quantity} for item in items]  # Return a list of items



@router.post("/add-item")
async def add_item(item: InventoryItemSchema, db: Session = Depends(get_db)):
    """
    Adds an item to the inventory.
    """
    existing_item = db.query(InventoryItem).filter(InventoryItem.name == item.name).first()
    
    if existing_item:
        raise HTTPException(status_code=400, detail="Item already exists")
    
    new_item = InventoryItem(name=item.name, quantity=item.quantity)
    db.add(new_item)
    db.commit()
    return {"message": f"Item '{item.name}' added"}

@router.delete("/remove-item/{item_name}")
async def remove_item(item_name: str, db: Session = Depends(get_db)):
    """
    Removes an item from the inventory.
    """
    item = db.query(InventoryItem).filter(InventoryItem.name == item_name).first()
    
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db.delete(item)
    db.commit()
    return {"message": f"Item '{item_name}' removed"}

@router.put("/update-quantity")
async def update_quantity(item: InventoryItemSchema, db: Session = Depends(get_db)):
    """
    Updates the quantity of an existing item.
    """
    existing_item = db.query(InventoryItem).filter(InventoryItem.name == item.name).first()
    
    if not existing_item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    existing_item.quantity = item.quantity
    db.commit()
    return {"message": f"Item '{item.name}' updated"}

