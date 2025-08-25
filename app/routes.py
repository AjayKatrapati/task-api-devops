from flask import Blueprint, jsonify, request
from .models import Task, db

bp = Blueprint('routes', __name__)

@bp.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([
        {
            "id": t.id,
            "title": t.title,
            "description": t.description,
            "done": t.done
        }
        for t in tasks
    ])

@bp.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    task = Task(
        title=data['title'],
        description=data.get('description', ''),
        done=False
    )
    db.session.add(task)
    db.session.commit()
    return jsonify({
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "done": task.done
    }), 201
