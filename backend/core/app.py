from flask import Flask

# Route imports
from backend.routes.user import users_bp
from backend.routes.home import home_bp

# logging
from backend.core.logger import Logger, LoggingLevel

app = Flask(__name__)

# Route register
app.register_blueprint(home_bp)  # Blueprint for the home route
app.register_blueprint(users_bp)  # Blueprint for all the user routes


class App:  # Defining App Class
    def __init__(self, flask_app: Flask):
        self.app = flask_app  # App variable for interaction with the flask app
        self.logger = Logger()
        self.config_path = '../../config/config.json'

    # TODO: Configuration-File

    def get_config(self):
        pass

    def run(self):
        self.logger.log('Server is starting', logging_level=LoggingLevel.INFO)
        self.app.run(  # running flask app with properties
            host='0.0.0.0',
            port=1337,
            debug=True,
            threaded=False
        )
