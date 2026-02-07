from fastapi import FastAPI
from .routes import cliente_routes, vendedor_routes
app = FastAPI()

app.include_router(cliente_routes.router)

app.include_router(vendedor_routes.router)

#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: str | None = None):
#    return {"item_id": item_id, "q": q}