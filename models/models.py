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
    
    def checkUser(self, usuario, password):
        self.cursor.execute(f'SELECT usuario_id FROM Usuarios WHERE Usuarios.usuario = "{usuario}" AND Usuarios.password = "{password}"')
        exists = self.cursor.fetchone()

        if exists:
            return exists
        
        return False



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

    def searchPostOne(self, titulo, usuario_id):
            self.cursor.execute(
                f"SELECT * FROM Posts WHERE Posts.usuario_id={usuario_id} AND Posts.titulo='{titulo}'"
            )
            return self.cursor.fetchone()

    def deletePost(self, titulo, usuario_id):
            self.cursor.execute(
                f"DELETE FROM Posts WHERE  Posts.usuario_id={usuario_id} AND Posts.titulo='{titulo}'"
            )
            self.mybasededatos.commit()
            return self.cursor.rowcount > 0

    def updatePost(self, usuario_id, tituloDB, titulo, contenido):
        self.cursor.execute(f'SELECT post_id FROM Posts WHERE Posts.usuario_id={usuario_id} AND Posts.titulo="{tituloDB}"')
        results =  self.cursor.fetchone()
        post_id = results.get('post_id')

        if results == None:
            return 'No se ha encontrado el usuario'

        if titulo and contenido:
            sql = (
                "UPDATE Posts SET titulo = %s, contenido = %s WHERE Posts.post_id = %s"
            )
            valores = (titulo, contenido, post_id)
            self.cursor.execute(sql, valores)
            self.mybasededatos.commit()
            return self.cursor.rowcount > 0

        if titulo:
            sql = "UPDATE Posts SET titulo = %s WHERE Posts.post_id = %s"
            valores = (titulo, post_id)
            self.cursor.execute(sql, valores)
            self.mybasededatos.commit()
            return self.cursor.rowcount > 0

        if contenido:
            sql = "UPDATE Posts SET contenido = %s WHERE Posts.post_id = %s"
            valores = (contenido, post_id)
            self.cursor.execute(sql, valores)
            self.mybasededatos.commit()
            return self.cursor.rowcount > 0

