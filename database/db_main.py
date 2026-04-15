import psycopg
from os import getenv

def db_connect():
    conn = psycopg.connect(dbname=getenv('DB_NAME'), port=getenv('DB_PORT'), user=getenv('DB_USER'), password=getenv('DB_PASSWORD'), host=getenv('DB_HOST'))
    cur = conn.cursor()
    return conn, cur


def table_create():
    conn, cur = db_connect()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS tasks_table
    (id SMALLSERIAL PRIMARY KEY,
        text varchar(255) NOT NULL,
        date TIMESTAMP NOT NULL,
        status boolean NOT NULL
    )
    ''')
    conn.commit()
    conn.close()


def table_add(task):
    conn, cur = db_connect()
    cur.execute('''
    INSERT INTO tasks_table
        (text, date, status)
        VALUES (%s, CURRENT_TIMESTAMP(0), %s)
    ''', (task, False))
    conn.commit()
    conn.close()

def table_list():
    conn, cur = db_connect()
    cur.execute('''
                SELECT * FROM tasks_table
                ORDER BY id
                ''')
    tasks_list = cur.fetchall()
    conn.close()
    return tasks_list

def task_done(task_id):
    conn, cur = db_connect()
    cur.execute('''
                UPDATE tasks_table
                SET status = %s
                WHERE id = %s;
                ''', (True, task_id))
    conn.commit()
    conn.close()

def task_delete(task_id):
    conn, cur = db_connect()
    cur.execute('''
                DElETE FROM tasks_table
                WHERE id = %s;
                ''', (task_id,))
    conn.commit()
    conn.close()