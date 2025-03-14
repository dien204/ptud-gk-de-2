from flask_login import UserMixin
from datetime import datetime
from werkzeug.utils import secure_filename
from flask import current_app
from . import db
import os

# Bảng User
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    avatar = db.Column(db.String(300), default="default_avatar.png")
    tasks = db.relationship('Task', backref='owner', lazy=True)

    def set_avatar(self, file):
        filename = secure_filename(file.filename)
        avatar_path = os.path.join('static/uploads', filename)
        file.save(os.path.join(current_app.root_path, avatar_path))
        self.avatar = avatar_path  # Cập nhật đường dẫn avatar
        db.session.commit()

# Bảng Task
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(50), nullable=False, default='Pending')  # Pending, In Progress, Completed
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    finished_at = db.Column(db.DateTime, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def mark_completed(self):
        self.status = 'Completed'
        self.finished_at = datetime.utcnow()
