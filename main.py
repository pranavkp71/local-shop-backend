from fastapi import FastAPI
from routers import shops, categories, areas, admin

app = FastAPI(title="Local Shop Listing API")

app.include_router(shops.router)
app.include_router(categories.router)
app.include_router(areas.router)
app.include_router(admin.router)

@app.get("/")
def home():
    return {"message": "API is running"}
