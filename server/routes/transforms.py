from fastapi import APIRouter
from server.models import Transform

router = APIRouter()

@router.post("/transform")
async def update_transform(transform: Transform):
    """
    Receives full transform data (position, rotation, scale).
    """
    print(f"Received transform: {transform}")
    return {"message": "Transform data received", "data": transform}

@router.post("/translation")
async def update_translation(position: tuple[float, float, float]):
    """
    Receives only position data.
    """
    print(f"Received position: {position}")
    return {"message": "Position data received", "position": position}

@router.post("/rotation")
async def update_rotation(rotation: tuple[float, float, float]):
    """
    Receives only rotation data.
    """
    print(f"Received rotation: {rotation}")
    return {"message": "Rotation data received", "rotation": rotation}

@router.post("/scale")
async def update_scale(scale: tuple[float, float, float]):
    """
    Receives only scale data.
    """
    print(f"Received scale: {scale}")
    return {"message": "Scale data received", "scale": scale}
