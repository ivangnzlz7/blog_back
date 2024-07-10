from flask import Blueprint, request, jsonify
from models.models import Usuarios

user = Blueprint('user', __name__)

userAdmin = Usuarios()

@user.route('/')
def home():
    return '<h1>Servidor funcionando</h1>'

@user.route('/add', methods=['POST'])
def addUser(): 
    usuario = request.form['usuario']
    email = request.form['email']
    password = request.form['password']

    newUser = userAdmin.add_user(usuario, email, password)
    return jsonify(newUser)


@user.route('/update', methods=['PUT'])
def modify():
    usuario = request.form['usuario']
    password = request.form['password']

    userUp = userAdmin.modify_password(usuario, password)
    return jsonify(userUp)

@user.route('/check', methods=['POST'])
def checkUser():
    usuario = request.form['usuario']
    password = request.form['password']

    userChek = userAdmin.checkUser(usuario, password)
    return jsonify(userChek)