from app.data.conect import connect_to_db
import psycopg2



def create_table():
    commands = (
        """
        CREATE TABLE IF NOT EXISTS users (
            tg_id INTEGER PRIMARY KEY UNIQUE NOT NULL,
            subscribe BOOLEAN NOT NULL DEFAULT FALSE
        );
        """,

        """
        CREATE TABLE IF NOT EXISTS subsctibes (
            owner_tg_td INTEGER REFERENCES users(tg_id) UNIQUE NOT NULL,
            start_date TIMESTAMP NOT NULL,
            theEnd_date TIMESTAMP NOT NULL
        );
        """,

        """
        CREATE TABLE IF NOT EXISTS resepy (
            id SERIAL PRIMARY KEY UNIQUE NOT NULL,
            owner_tg_id INTEGER REFERENCES users(tg_id) NOT NULL,
            category TEXT[] NOT NULL,
            name TEXT NOT NULL,
            cooking TEXT[] NOT NULL,
            photo BYTEA[],
            likes INTEGER NOT NULL DEFAULT 0 
        );
        """,

        """
        CREATE TABLE IF NOT EXISTS user_likes (
            owner_tg_id INTEGER REFERENCES users(tg_id),
            resepy_id INTEGER REFERENCES resepy(id) ON UPDATE CASCADE ON DELETE CASCADE
        );
        """
    )

    conn = None

    try:
        conn, cur = connect_to_db()

        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DataError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()