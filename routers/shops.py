from fastapi import APIRouter, HTTPException
from supabase_cliendt import supabase
from models.schemas import Shops

router = APIRouter(prefix="api/shops", tags=["Shops"])

@router.get("/")
def get_shops():
    response = supabase.table("shops").select("*").execute()
    return response.data

@router.get("/{shop_id}")
def get_shop(shop_id: str):
    res = supabase.table("shops").select("*").eq("id", shop_id).execute()
    if not res.data:
        raise HTTPException(status_code=404, detail="Shop not found")
    return res.data[0]

@router.post("/")
def add_shop(shop: Shops):
    data = shop.dict()
    response = supabase.table("shops").insert(data).execute()
    return {"message": "Shop added sucessfully", "data": response.data}