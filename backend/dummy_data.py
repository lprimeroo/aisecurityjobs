from flask import Flask
from models import Job, db  # Import the Job model and the db object from your models module

app = Flask(__name__)

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
    add_dummy_jobs()