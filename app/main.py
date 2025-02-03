from fastapi import FastAPI
import string
import random
from app.dp import create_url

app = FastAPI()

def generate_short_url(length: int = 6):
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))

@app.post("/shorten/")
async def shorten_url(original_url: str):
    short_url = generate_short_url()
    await create_url(original_url, short_url)
    return {"shortened_url": f"http://localhost:8000/{short_url}"}