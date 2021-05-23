from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

class config():
    DEBUG =True
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/info16"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

app.config.from_object(config)
db = SQLAlchemy(app)





@app.route('/')
def index():
    return 'index11111'


if __name__ == '__main__':
    app.run()
