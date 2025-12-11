from flask import Blueprint, render_template
import json

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    with open('app/data/blogs.json') as f:
        blogs = json.load(f)[:3]  # Latest 3
    return render_template('home.html', blogs=blogs)

@main_bp.route('/about')
def about():
    return render_template('about.html')

@main_bp.route('/hire')
def hire():
    return render_template('hire.html')
