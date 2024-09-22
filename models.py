from app import db
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    projects = relationship('Project', backref='user', lazy=True)

class Project(db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    # description = db.Column(db.Text)
    user_id = db.Column('userId', db.Integer, db.ForeignKey('user.id'), nullable=False)
    tasks = relationship('Task', backref='project', lazy=True)

class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    project_id = db.Column('projectId', db.Integer, db.ForeignKey('project.id'), nullable=False)
