from flask import Blueprint, request, jsonify
from models.models import  Posts

posts = Blueprint("posts", __name__)

post = Posts()


@posts.route('/user/<int:usuario>/posts/<int:post_id>', methods=['GET', 'DELETE'])
def postONe(usuario, post_id):
    if request.method == 'DELETE':
        postDelete = post.deletePost(post_id, usuario)
        return jsonify(postDelete)
    
    postOne = post.searchPostOne(post_id, usuario)
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


@posts.route('/post/<int:post_id>', methods=['PUT'])
def updatePost(post_id):
    titulo = request.form['titulo']
    contenido = request.form['contenido']

    postUp = post.updatePost(post_id, titulo, contenido)
    return jsonify(postUp)

