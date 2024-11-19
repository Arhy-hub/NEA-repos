from flask import Flask
#function that runs the api, importing it and then init manages it, turning website into python package
def create_api():
    api = Flask(__name__)
    
    api.config['SECRET_KEY'] = 'Password123!'

    from .views import views
    from .authentication import authentication
    from .pipe_fin_data import pipe_fin_data

    api.register_blueprint(views,url_prefix='/')
    api.register_blueprint(authentication, url_prefix='/')
    api.register_blueprint(pipe_fin_data, url_prefix='/')
    

    return api