from fastapi import APIRouter
from supabase_client import supabase
from models.schemas import Area

router = APIRouter(prefix="/api/areas", tags=["Areas"])

@router.get("/")
def get_areas():
    return supabase.table("areas").select("*").execute().data

@router.post("/")
def add_area(area: Area):
    return supabase.table("areas").insert(area.dict()).execute().data
