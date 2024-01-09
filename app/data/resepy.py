from app.data.conect import connect_to_db
import psycopg2


async def add_recipe(owner_tg_id, category, name, cooking, photo=None):
    conn = None
    try:
        conn, cur = connect_to_db()
        
        cur.execute("INSERT INTO resepy (owner_tg_id, category, name, cooking, photo) VALUES (%s, %s, %s, %s, %s)",
                    (owner_tg_id, category, name, cooking, photo))
        
        conn.commit()
        print("Рецепт успешно добавлен!")
    except (Exception, psycopg2.Error) as error :
        print("Ошибка при добавлении рецепта:", error)
    finally:
        if conn is not None:
            conn.close()



async def update_recipe(recipe_id, owner_tg_id, category, name, cooking, photo=None):
    conn = None
    try:
        conn, cur = connect_to_db()
        
        cur.execute("UPDATE resepy SET owner_tg_id = %s, category = %s, name = %s, cooking = %s, photo = %s WHERE id = %s",
                    (owner_tg_id, category, name, cooking, photo, recipe_id))
        
        conn.commit()
        print("Рецепт успешно обновлен!")
    except (Exception, psycopg2.Error) as error :
        print("Ошибка при обновлении рецепта:", error)
    finally:
        if conn is not None:
            conn.close()




async def update_recipe_param(recipe_id, param_name, param_value):
    conn = None
    try:
        conn, cur = connect_to_db()
        
        cur.execute(f"UPDATE resepy SET {param_name} = %s WHERE id = %s", (param_value, recipe_id))
        
        conn.commit()
        print("Параметр рецепта успешно обновлен!")
    except (Exception, psycopg2.Error) as error :
        print(f"Ошибка при обновлении параметра рецепта {param_name}:", error)
    finally:
        if conn is not None:
            conn.close()


def get_recipes_by_owner(owner_tg_id):
    conn = None
    try:
        conn = psycopg2.connect(database="your_database", user="your_user", password="your_password", host="your_host", port="your_port")
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM resepy WHERE owner_tg_id = %s", (owner_tg_id,))
        recipes = cur.fetchall()
        
        if len(recipes) > 0:
            print(f"Все рецепты владельца с owner_tg_id = {owner_tg_id}:")
            for recipe in recipes:
                print(recipe)
        else:
            print(f"В базе данных нет рецептов с owner_tg_id = {owner_tg_id}")
    except (Exception, psycopg2.Error) as error :
        print("Ошибка при получении рецептов:", error)
    finally:
        if conn is not None:
            conn.close()