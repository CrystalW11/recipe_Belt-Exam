from flask import Flask
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.secret_key = "this is a secret"
bcrypt = Bcrypt(app)
