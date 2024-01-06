from environs import Env
from dataclasses import dataclass

@dataclass
class DB:
    host: str
    port: str
    user: str
    password: str
    db_name: str

def get_db_settings(path: str):
    env = Env()
    env.read_env(path)

    return DB(
            host=env.str('HOST'),
            port=env.str('PORT'),
            user=env.str('USER'),
            password=env.str('PASSWORD'),
            db_name=env.str('DB_NAME')
    )