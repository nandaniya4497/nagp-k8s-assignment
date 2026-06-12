import os
from psycopg2.pool import SimpleConnectionPool
from psycopg2.extras import RealDictCursor

pool = None


def get_pool():
    global pool
    if pool is None:
        pool = SimpleConnectionPool(
            minconn=1,
            maxconn=10,
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
        )
    return pool


def get_connection():
    conn = get_pool().getconn()
    return conn


def release_connection(conn):
    get_pool().putconn(conn)


def get_data():
    conn = get_connection()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                """
                SELECT id, name, department
                FROM employees
                ORDER BY id
                """
            )
            return [dict(row) for row in cursor.fetchall()]
    finally:
        release_connection(conn)
