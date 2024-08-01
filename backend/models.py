from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=True, nullable=False)
    salary_range = db.Column(db.String(50), nullable=True)
    location = db.Column(db.String(50), nullable=True)
    company = db.Column(db.String(50), nullable=True)
    date_posted = db.Column(db.DateTime, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'salary_range': self.salary_range,
            'location': self.location,
            'company': self.company,
            'date_posted': self.date_posted
        }
    
    def __repr__(self):
        return '<Job %r>' % self.title
