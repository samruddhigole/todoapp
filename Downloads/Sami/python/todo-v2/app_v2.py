from flask import Flask, render_template, request, jsonify, json
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_serialize import FlaskSerializeMixin


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://todouser:admin123@localhost:5432/todo"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

FlaskSerializeMixin.db = db  #created object

@app.route("/task", methods=["POST"])
def create_task():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            print (data['status'],data)
            new_task = Task(status=data['status'],description=data['description'])
            db.session.add(new_task)
            db.session.commit()
            return {"success":"SUCCESS"}
        else:
            return {"Result":"Not updated"}


@app.route("/task", methods=["GET"])
def get_task_list():
    tasks = Task.query.all()
    results = [
            {
                "id" : task.id,
                "description" : task.description,
                "status": task.status
                }
            for task in tasks]
    return {"count":len(results), "task":results}



@app.route("/task/<int:id>", methods=["GET"])
def handle_task_by_id(id):

    task = Task.query.get_or_404(id)

    result ={
            "id": task.id,
            "description" : task.description,
            "status" : task.status}
    return {"message": "success", "task": result}


@app.route("/task/<int:id>", methods=["DELETE"])

def delete_by_id(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    result ={
             "id": task.id,
             "description" : task.description,
             "status" : task.status}
    return {"message": "success", "task": result}


@app.route("/task/<int:id>", methods=["PUT"])

def update_task(id):

    task = Task.query.get_or_404(id)
    tasks = request.get_json()
    task.description = tasks['description']
    task.status = tasks['status']
    db.session.add(task)
    db.session.commit()
    return {"message": "task is updated"}



class Task(FlaskSerializeMixin, db.Model):
    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String())
    status = db.Column(db.Boolean())

    serialise_only=('description','status')

    # serializer fields
    create_fields = update_fields = ['description','status']

    def __init__(self, description, status):
        self.description = description
        self.status = status
db.create_all()
db.session.commit()


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=8080)
