from flask import Flask, jsonify, request
from models import Job, db  # Assuming Job is the model for a job listing
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'  # Replace with your database URI
db.init_app(app)

@app.route('/jobs', methods=['GET'])
def get_jobs():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    jobs = Job.query.paginate(page=page, per_page=per_page, error_out=False)
    return jsonify([job.to_dict() for job in jobs.items])

@app.route('/jobs/<int:job_id>', methods=['GET'])
def get_job(job_id):
    job = Job.query.get_or_404(job_id)
    return jsonify(job.to_dict())

@app.route('/jobs/search', methods=['GET'])
def search_jobs():
    query = request.args.get('q', '')
    jobs = Job.query.filter(Job.title.contains(query)).all()
    return jsonify([job.to_dict() for job in jobs])

@app.route('/jobs', methods=['POST'])
def add_job():
    job = Job.from_dict(request.json)
    db.session.add(job)
    db.session.commit()
    return jsonify(job.to_dict()), 201

def add_dummy_jobs():
    dummy_jobs = [
        {'title': 'Software Engineer', 'description': 'Develop and maintain software applications.'},
        {'title': 'Data Scientist', 'description': 'Analyze and interpret complex data.'},
    ]

    with app.app_context():
        for job_data in dummy_jobs:
            job = Job(**job_data)
            db.session.add(job)

        db.session.commit()

if __name__ == "__main__":
    app.run()
# if __name__ == "__main__":
#     with app.app_context():
#         add_dummy_jobs()