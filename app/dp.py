import asyncpg
from typing import Optional

DATABASE_URL = "postgresql://postgres:password@localhost:5432/url_shortener_py"

async def get_db_connection():
    return await asyncpg.connect(DATABASE_URL)

async def create_url(original_url: str, short_url: str):
    conn = await get_db_connection()
    await conn.execute(
        "INSERT INTO urls (original_url, short_url) VALUES ($1, $2)",
        original_url, short_url
    )
    await conn.close()

async def get_url_by_short(short_url: str) -> Optional[str]:
    conn = await get_db_connection()
    result = await conn.fetchrow(
        "SELECT original_url FROM urls WHERE short_url = $1", short_url
    )
    await conn.close()
    return result['original_url'] if result else None