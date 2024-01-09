from data.conect import connect_to_db
import psycopg2

async def add_user(owner_tg_td, start_date, theEnd_date):
    conn = None
    try:
        conn, cur = connect_to_db()

        # добавить проверку на существование такого элемента и если есть, то изменить его, если нет, создать новый
        
        cur.execute("INSERT INTO subsctibes (owner_tg_td, start_date, theEnd_date) VALUES (%s, %s, %s)",
                    (owner_tg_td, start_date, theEnd_date))
        
        conn.commit()
        print("User успешно добавлен!")
    except (Exception, psycopg2.Error) as error :
        print("Ошибка при добавлении user:", error)
    finally:
        if conn is not None:
            conn.close()