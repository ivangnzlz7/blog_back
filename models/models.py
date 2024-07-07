import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ['MYSQL_USER']
password = os.environ['MYSQL_PASSWORD']
host = os.environ['MYSQL_HOST']
database = os.environ['MYSQL_DATABASE']


class Usuarios:

    def __init__(self):

        self.mybasededatos = mysql.connector.connect(
            host=host, user=user, password=password, database=database
        )

        self.cursor = self.mybasededatos.cursor()

        self.cursor.execute("USE blog_proyect")

        self.mybasededatos.commit()

        self.cursor.close()
        self.cursor = self.mybasededatos.cursor(dictionary=True)

    def add_user(self, usuario, email, password):
        self.cursor.execute(f'SELECT * FROM Usuarios WHERE Usuarios.usuario = "{usuario}"')
        exists = self.cursor.fetchone()

        if exists:
            return f'El usuario {usuario} ya existe'
        
        sql = "INSERT INTO Usuarios(usuario, email, password) VALUES (%s, %s, %s)"
        valores = (usuario, email, password)

        self.cursor.execute(sql, valores)
        self.mybasededatos.commit()
        return self.cursor.lastrowid 
    
    def modify_password(self, usuario, password):
        self.cursor.execute(f'SELECT * FROM Usuarios WHERE Usuarios.usuario = "{usuario}"')
        exists = self.cursor.fetchone()

        if exists:
            sql = (
                "UPDATE Usuarios SET password = %s WHERE Usuarios.usuario = %s "
            )
            valores = (password, usuario)
            self.cursor.execute(sql, valores)
            self.mybasededatos.commit()
            return self.cursor.rowcount > 0
        
        return f'{usuario} no Existe'



class Posts:

    def __init__(self):

        self.mybasededatos = mysql.connector.connect(
            host=host, user=user, password=password, database=database
        )

        self.cursor = self.mybasededatos.cursor()

        self.cursor.execute("USE blog_proyect")

        self.mybasededatos.commit()
        self.cursor.close()
        self.cursor = self.mybasededatos.cursor(dictionary=True)

    def add_post(self, usuario_id, titulo, contenido):
        sql = 'INSERT INTO Posts(usuario_id, titulo, contenido) VALUES(%s, %s, %s)'
        valores = (usuario_id, titulo, contenido)
        self.cursor.execute(sql, valores)
        self.mybasededatos.commit()
        return self.cursor.lastrowid

    def searchPostAll(self, usuario_id):
            self.cursor.execute(
                f"SELECT * FROM Posts WHERE Posts.usuario_id={usuario_id}"
            )
            return self.cursor.fetchall()

    def searchPostOne(self, postID, usuario_id):
            self.cursor.execute(
                f"SELECT * FROM Posts WHERE Posts.post_id={postID} AND Posts.usuario_id={usuario_id}"
            )
            return self.cursor.fetchone()

    def deletePost(self, postID, usuario_id):
            self.cursor.execute(
                f"DELETE FROM Posts WHERE Posts.post_id={postID} AND Posts.usuario_id={usuario_id}"
            )
            self.mybasededatos.commit()
            return self.cursor.rowcount > 0

    def updatePost(self, postID, titulo=None, contenido=None):

        if titulo != None and contenido != None:
            sql = (
                "UPDATE Posts SET titulo = %s, contenido = %s WHERE Posts.post_id = %s"
            )
            valores = (titulo, contenido, postID)
            self.cursor.execute(sql, valores)
            self.mybasededatos.commit()
            return self.cursor.rowcount > 0

        if titulo != None:
            sql = "UPDATE Posts SET titulo = %s WHERE Posts.post_id = %s"
            valores = (titulo, postID)
            self.cursor.execute(sql, valores)
            self.mybasededatos.commit()
            return self.cursor.rowcount > 0

        if contenido != None:
            sql = "UPDATE Posts SET contenido = %s WHERE Posts.post_id = %s"
            valores = (contenido, postID)
            self.cursor.execute(sql, valores)
            self.mybasededatos.commit()
            return self.cursor.rowcount > 0
