from flask import Blueprint , render_template

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/About')
def about():
    return render_template("about.html")

@views.route('/Services')
def service():
    return render_template("services.html")

@views.route('/Contact')
def contact():
    return render_template("contact.html")