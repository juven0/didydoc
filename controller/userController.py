from database.database import get_db

class UsersController:

    def __init__(self, db) -> None:
        self.db = db

def create(self ,pseudo, email, password) -> bool:
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO users(username, email, password) VALUES (?, ?, ?)"
    cursor.execute(statement, [pseudo, email, password])
    db.commit()
    return True

def ged_by_id(self, id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECTE * FROM user WHERE id=?"
    cursor.execute(statement, [id])
    return cursor.fetchone()

def ged_by_username(self, username):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECTE * FROM users WHERE username=?"
    cursor.execute(statement, [username])
    return cursor.fetchone()

def get_All(self):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM users"
    cursor.execute(query)
    return cursor.fetchall()