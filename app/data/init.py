from environs import Env
from dataclasses import dataclass

from settings import get_db_settings

import psycopg2
import logging


db = get_db_settings(".env")



try:
    connection = psycopg2.connect(
        host=db.host,
        port=db.port,
        user=db.user,
        password=db.password,
        database=db.db_name
    )

    # cursor = connection.cursor()

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )

        print(f"Server version: {cursor.fetchone()}")



except Exception as e:
    print("Failed connection to database")
finally:
    if connection:
        # cursor.close()
        connection.close()
        print("Connection closed")
        