from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post("/shorten/")
async def create_short_url(original_url: str):
    pass