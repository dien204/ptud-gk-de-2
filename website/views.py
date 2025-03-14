from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import db, Task
from datetime import datetime
from werkzeug.utils import secure_filename
import os

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    filter_status = request.args.get('status', 'All')
    
    if filter_status == 'All':
        tasks = Task.query.filter_by(user_id=current_user.id).all()
    else:
        tasks = Task.query.filter_by(user_id=current_user.id, status=filter_status).all()

    return render_template('home.html', tasks=tasks, filter_status=filter_status)

@views.route('/create_task', methods=['GET', 'POST'])
@login_required
def create_task():
    if request.method == 'POST':
        title = request.form['title'] 
        description = request.form['description']
        status = request.form['status']
        
        new_task = Task(title=title, description=description, status=status, user_id=current_user.id)
        if new_task.status == 'Completed':
            new_task.mark_completed()

        db.session.add(new_task)
        db.session.commit()
        flash('Task created successfully!', 'success')
        return redirect(url_for('views.home'))
    
    return render_template('create_task.html')

@views.route('/edit_task/<int:task_id>', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.user_id != current_user.id:
        flash('Unauthorized access!', 'danger')
        return redirect(url_for('views.home'))

    if request.method == 'POST':
        task.title = request.form['title']
        task.description = request.form['description']
        task.status = request.form['status']
        if task.status == 'Completed':
            task.finished_at = datetime.utcnow()
        db.session.commit()
        flash('Task updated successfully!', 'success')
        return redirect(url_for('views.home'))

    return render_template('edit_task.html', task=task)

@views.route('/delete_task/<int:task_id>', methods=['POST'])
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.user_id != current_user.id:
        flash('Unauthorized access!', 'danger')
        return redirect(url_for('views.home'))

    db.session.delete(task)
    db.session.commit()
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('views.home'))

UPLOAD_FOLDER = 'static\\uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@views.route('/upload_avatar', methods=['GET', 'POST'])
@login_required
def upload_avatar():
    if request.method == 'POST':
        if 'avatar' not in request.files:
            flash("Không tìm thấy file!", "danger")
            return redirect(request.url)

        file = request.files['avatar']

        if file.filename == '':
            flash("Chưa chọn file!", "danger")
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)

            file.save(os.path.join(os.getcwd(), file_path))

            # current_user.set_avatar(file_path)

            flash("Cập nhật avatar thành công!", "success")
            return redirect(url_for('auth.upload_avatar'))

    return render_template('upload_avatar.html')