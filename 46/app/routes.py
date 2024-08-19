# app/routes.py
from flask import Blueprint, render_template, flash, redirect, url_for, request
from werkzeug.utils import secure_filename
from .forms import UploadForm
from .config import Config
import os

main_bp = Blueprint('main', __name__)

@main_bp.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        file.save(os.path.join(Config.UPLOAD_FOLDER, filename))
        flash(f'File "{filename}" uploaded successfully!', 'success')
        return redirect(url_for('main.upload'))
    return render_template('upload.html', form=form)
