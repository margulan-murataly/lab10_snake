import psycopg2
from config import load_config


def insert_user_and_score(username, score):

    sql = """INSERT INTO users(username)
             VALUES(%s) RETURNING user_id;"""

    contact_id = None
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:  
                cur.execute(sql, (username,))

                rows = cur.fetchone()
                if rows:
                    user_id = rows[0]
                    
                cur.execute(
                    "INSERT INTO scores (user_id, score) VALUES (%s, %s)",
                    (user_id, score)
                )

                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return user_id

if __name__ == '__main__':
    
    insert_user_and_score(username, score)