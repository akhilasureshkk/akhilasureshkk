from flask import Flask
from app.urls import app_blueprint  

mage_app = Flask(__name__)

# Register the app_blueprint with the app
mage_app.register_blueprint(app_blueprint, url_prefix='/app')

if __name__ == '__main__':
    mage_app.run(host='0.0.0.0',debug=True,port=5466)