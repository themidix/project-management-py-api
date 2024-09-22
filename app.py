from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import Config

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)
jwt = JWTManager(app)

from routes import auth_blueprint, project_blueprint, task_blueprint, greeting_blueprint
app.register_blueprint(auth_blueprint, url_prefix="/auth")
app.register_blueprint(project_blueprint, url_prefix="/projects")
app.register_blueprint(task_blueprint, url_prefix="/tasks")
app.register_blueprint(greeting_blueprint, url_prefix="/greeting")

if __name__ == '__main__':
    app.run(debug=True)
