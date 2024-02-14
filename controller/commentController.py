from database.database import get_db

class Comments:
    def __init__(self, db) -> None:
        self.db = db

    def create(self ,idUser,idpost ,content):
        db = get_db()
        cursor = db.cursor()
        statement = "INSERT INTO comments(user_id,post_id , content) VALUES (?, ?, ?)"
        cursor.execute(statement, [idUser,idpost, content])
        db.commit()
        return True


    def get_by_id(self, id):
        db = get_db()
        cursor = db.cursor()
        statement = "SELECT * FROM comments WHERE id = ?"
        cursor.execute(statement, [id])
        return cursor.fetchone()


    def get_All_by_postId(self, id):
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM comments WHERE post_id  = ?"
        cursor.execute(query, [id])
        return cursor.fetchall()