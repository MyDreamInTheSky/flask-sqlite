from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../tmp/test.db'
app.config['SECRET_KEY'] = 'Chucthanhlam1907'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
