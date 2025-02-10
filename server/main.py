from fastapi import FastAPI
from server.routes import transforms, inventory  # Import inventory API

app = FastAPI()

# Register API routes
app.include_router(transforms.router)
app.include_router(inventory.router)


@app.get("/")
async def root():
    return {"message": "DCC Integration API is running!"}

@app.get("/inventory")
def get_inventory(cursor):
    cursor.execute("SELECT name, quantity FROM inventory")
    items = cursor.fetchall()
    inventory_list = [{"name": item[0], "quantity": item[1]} for item in items]
    return inventory_list  # This should be a list, NOT a string
