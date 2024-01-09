from app.settings import settings
import asyncio
import psycopg2


async def connect_to_db():
    params = {
        'host': settings.db.host,
        'database': settings.db.db_name,
        'user': settings.db.user,
        'password': settings.db.password,
    }
    conn = psycopg2.connect(**params)
    cur = conn.cursor()

    return conn, cur
