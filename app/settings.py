from environs import Env
from dataclasses import dataclass
from data.settings import DB, get_db_settings


@dataclass
class Bots:
    token: str
    admin_id: int



@dataclass
class Settings:
    bots: Bots
    db: DB


def get_settings(path: str):
    env = Env()
    env.read_env(path)

    db = get_db_settings(path)

    return Settings(
        bots=Bots(
            token=env.str('TOKEN'),
            admin_id=env.int('ADMIN')
        ),
        db=db
    )

settings = get_settings('.env')