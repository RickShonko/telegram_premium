from database.db import conn, cursor

def add_user(telegram_id, username, first_name):
    cursor.execute("""
    INSERT OR IGNORE INTO users
    VALUES (?, ?, ?)
    """, (telegram_id, username, first_name))

    conn.commit()