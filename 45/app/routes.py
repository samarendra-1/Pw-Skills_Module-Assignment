# app/routes.py
from flask import Blueprint, render_template, flash, redirect, url_for
from .forms.py import MyForm

main_bp = Blueprint('main', __name__)

@main_bp.route('/form', methods=['GET', 'POST'])
def form():
    form = MyForm()
    if form.validate_on_submit():
        flash(f'Form submitted successfully with name: {form.name.data}', 'success')
        return redirect(url_for('main.form'))
    return render_template('form.html', form=form)

