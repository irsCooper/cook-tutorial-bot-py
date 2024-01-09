from app.data.conect import connect_to_db
import psycopg2

async def check_user():
    return None


async def add_user(tg_id):
    conn = None
    try:
        conn, cur = connect_to_db()
        
        cur.execute("INSERT INTO users (tg_id) VALUES (%s)",
                    (tg_id))
        
        conn.commit()
        print("User успешно добавлен!")
    except (Exception, psycopg2.Error) as error :
        print("Ошибка при добавлении user:", error)
    finally:
        if conn is not None:
            conn.close()


async def update_user_subscribe(tg_id, _bool):
    conn = None
    try:
        conn, cur = connect_to_db()

        # добавить проверку на существование подписки и сроки действия
        
        cur.execute("UPDATE users SET subscribe VALUES = %s WHERE id = %s", 
                    (_bool, tg_id))
        
        conn.commit()
        print("User успешно добавлен!")
    except (Exception, psycopg2.Error) as error :
        print("Ошибка при добавлении user:", error)
    finally:
        if conn is not None:
            conn.close()

