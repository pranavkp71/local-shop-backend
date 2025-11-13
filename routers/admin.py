from fastapi import APIRouter, HTTPException
from supabase_client import supabase
from models.schemas import Admin
import bcrypt

router = APIRouter(prefix="/api/admin", tags=["Admin"])

@router.post("/login")
def admin_login(credentials: Admin):
    result = supabase.table("admins").select("*").eq("email", credentials.email).execute()

    if not result.data:
        raise HTTPException(status_code=404, detail="Admin not found")

    admin = result.data[0]
    if bcrypt.checkpw(credentials.password.encode("utf-8"), admin["password_hash"].encode("utf-8")):
        return {"message": "Login successful", "admin": admin["email"]}
    else:
        raise HTTPException(status_code=401, detail="Invalid password")
