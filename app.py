import logging
from flask import Flask
from routes import api

FORMAT = '%(asctime)s|%(name)s|%(levelname)s|%(lineno)d|%(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)
LOGGER = logging.getLogger(__name__)
app = Flask(__name__)
app.register_blueprint(api.core)

if __name__ == "__main__":
    app.run(debug=True)
