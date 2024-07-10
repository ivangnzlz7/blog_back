from flask import Blueprint, request, jsonify
from models.models import  Posts

posts = Blueprint("posts", __name__)

post = Posts()
 

@posts.route('/user/<int:usuario>/posts', methods=['GET', 'DELETE'])
def postONe(usuario):

    titulo = request.form['titulo']
    if request.method == 'DELETE':
        postDelete = post.deletePost(titulo, usuario)
        return jsonify(postDelete)
    
    postOne = post.searchPostOne(titulo, usuario)
    return jsonify(postOne) 
 

@posts.route('/newPost/<int:usuario>', methods=['POST'])
def addPost(usuario):
    titulo = request.form['titulo']
    contenido = request.form['contenido']

    newPost = post.add_post(usuario, titulo, contenido)
    return jsonify(newPost)


@posts.route('/posts/<int:usuario_id>', methods=['GET'])
def postAll(usuario_id):
    posts = post.searchPostAll(usuario_id)
    return jsonify(posts)


@posts.route('/post/update/<int:usuario_id>', methods=['PUT'])
def updatePost(usuario_id):

    tituloDB = request.form['tituloDB']
    titulo = request.form['titulo']
    contenido = request.form['contenido']


    postUp = post.updatePost(usuario_id ,tituloDB, titulo, contenido)
    return jsonify(postUp)

