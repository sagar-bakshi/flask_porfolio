from flask import render_template
from app import app
from app.forms import ContactForm
from datetime import datetime


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/projects')
def projects():
    return render_template('projects.html', title='Projects')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Handle form submission, e.g., send an email, store data in a database, etc.
        return render_template('contact_success.html')
    return render_template('contact.html', form=form)


@app.route('/blog')
def blog():
    blog_posts = [
        {
            'title': 'My First Blog Post',
            'content': 'This is my first blog post as a cloud architect...',
            'date_posted': datetime(2023, 4, 15)
        },
        {
            'title': 'My Second Blog Post',
            'content': 'In this blog post, I will share my experience working with serverless architectures...',
            'date_posted': datetime(2023, 4, 17)
        }
    ]
    return render_template('blog.html', blog_posts=blog_posts)
