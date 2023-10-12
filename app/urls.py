from flask import Blueprint
from app import views

# Create a Blueprint for the app
app_blueprint = Blueprint('app', __name__ ,url_prefix='/app')

# Define your URL routes

app_blueprint.add_url_rule('/add_student', 'add_student', views.add_student, methods=['POST' , 'GET'])
app_blueprint.add_url_rule('/view_student', 'view_student', views.view_student, methods=['GET'])
app_blueprint.add_url_rule('/delete_student', 'delete_student', views.delete_student, methods=['POST'])