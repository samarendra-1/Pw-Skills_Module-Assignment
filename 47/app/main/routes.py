from flask import render_template
from app.main import main

@main.route('/')
def index():
    return "Hello from the main blueprint!"
