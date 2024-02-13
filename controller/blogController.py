from database.database import get_db

class PostController:
    def __init__(self, db) -> None:
        self.db = db
    def create(idUser, content,title, classename):
        db = get_db()
        cursor = db.cursor()
        statement = "INSERT INTO post(idUser,title, content, classename) VALUES (?,?, ?, ?)"
        cursor.execute(statement, [idUser,title, content, classename])
        db.commit()
        return True


    def get_by_id(self, id):
        db = get_db()
        cursor = db.cursor()
        statement = "SELECT * FROM post WHERE id = ?"
        cursor.execute(statement, [id])
        return cursor.fetchone()


    def get_All(self):
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM post"
        cursor.execute(query)
        return cursor.fetchall()