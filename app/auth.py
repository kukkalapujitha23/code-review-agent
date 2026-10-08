import sqlite3


def get_user(conn, username):
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM users WHERE name = ?", (username,))
    return cur.fetchone()
