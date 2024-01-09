from environs import Env
from dataclasses import dataclass


@dataclass
class Bots:
    token: str
    admin_id: int


@dataclass
class DB:
    host: str
    port: str
    user: str
    password: str
    db_name: str


@dataclass
class Settings:
    bots: Bots
    db: DB


def get_settings(path: str):
    env = Env()
    env.read_env(path)

    return Settings(
        bots=Bots(
            token=env.str('TOKEN'),
            admin_id=env.int('ADMIN')
        ),
        db=DB(
            host=env.str('HOST'),
            port=env.str('PORT'),
            user=env.str('USER'),
            password=env.str('PASSWORD'),
            db_name=env.str('DB_NAME')
        )
    )

settings = get_settings('.env')