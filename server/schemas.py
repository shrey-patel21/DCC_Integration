from pydantic import BaseModel

# Pydantic model for request validation
class InventoryItemSchema(BaseModel):
    name: str
    quantity: int
