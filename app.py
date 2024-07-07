from flask import Flask
from routes.posts import posts
from routes.users import user
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

app.register_blueprint(posts, url_prefix='/blog')
app.register_blueprint(user, url_prefix='/admin')

