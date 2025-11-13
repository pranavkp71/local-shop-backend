from fastapi import APIRouter
from supabase_client import supabase
from models.schemas import Categories

router = APIRouter(prefix="/api/categories", tags=["Categories"])

@router.get("/")
def get_categories():
    return supabase.table("categories").select("*").execute().data

@router.post("/")
def add_category(category: Categories):
    return supabase.table("categories").insert(category.dict()).execute().data
