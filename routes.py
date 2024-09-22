from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models import User, Project, Task, db
from werkzeug.security import generate_password_hash, check_password_hash
import logging

# Set up logging for routes
logger = logging.getLogger(__name__)

auth_blueprint = Blueprint('auth', __name__)
project_blueprint = Blueprint('projects', __name__)
task_blueprint = Blueprint('tasks', __name__)
greeting_blueprint = Blueprint('greeting', __name__)

@greeting_blueprint.route('/', methods=['GET'])
def home():
    return "Hello World"

# User Registration
# User Registration
@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
    new_user = User(email=data['email'], password=hashed_password)
    
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully!"}), 201
    except Exception as e:
        return jsonify({"message": "Registration failed!", "error": str(e)}), 500

# User Login
@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=user.id)
        logger.info(f"User logged in: {data['email']}")
        return jsonify(access_token=access_token), 200
    else:
        logger.warning(f"Failed login attempt for user: {data['email']}")
        return jsonify({"message": "Invalid credentials!"}), 401

# Create Project
@project_blueprint.route('/', methods=['POST'])
@jwt_required()
def create_project():
    data = request.get_json()
    user_id = get_jwt_identity()
    new_project = Project(name=data['name'], user_id=user_id)
    
    try:
        db.session.add(new_project)
        db.session.commit()
        logger.info(f"Project created by user {user_id}: {data['name']}")
        return jsonify({"message": "Project created successfully!"}), 201
    except Exception as e:
        logger.error(f"Error while creating project: {e}")
        return jsonify({"message": "Project creation failed!"}), 500

# CRUD for tasks (similar to projects)
@task_blueprint.route('/<int:projectId>', methods=['POST'])
@jwt_required()
def add_task(projectId):
    data = request.get_json()
    new_task = Task(name=data['name'], description=data['description'], project_id=projectId)
    
    try:
        db.session.add(new_task)
        db.session.commit()
        logger.info(f"Task added to project {projectId}: {data['name']}")
        return jsonify({"message": "Task added successfully!"}), 201
    except Exception as e:
        logger.error(f"Error while adding task to project {projectId}: {e}")
        return jsonify({"message": "Task addition failed!"}), 500

