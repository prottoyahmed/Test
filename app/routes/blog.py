from flask import Blueprint, render_template, abort
import json
import markdown

blog_bp = Blueprint('blog', __name__)

@blog_bp.route('/')
def blog_list():
    with open('app/data/blogs.json') as f:
        blogs = json.load(f)
    return render_template('blog/list.html', blogs=blogs)

@blog_bp.route('/<slug>')
def blog_detail(slug):
    with open('app/data/blogs.json') as f:
        blogs = json.load(f)
    blog = next((b for b in blogs if b['slug'] == slug), None)
    if not blog:
        abort(404)
    blog['content_html'] = markdown.markdown(blog['content'])
    return render_template('blog/detail.html', blog=blog)
