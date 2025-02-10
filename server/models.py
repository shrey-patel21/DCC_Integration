from pydantic import BaseModel
from typing import Optional

# Model for object transformations
class Transform(BaseModel):
    position: tuple[float, float, float]
    rotation: tuple[float, float, float]
    scale: tuple[float, float, float]

# Model for inventory items
class InventoryItem(BaseModel):
    name: str
    quantity: int
    description: Optional[str] = None
