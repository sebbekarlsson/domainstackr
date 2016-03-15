from flask import Flask

from domainstackr.views.index import bp as index_bp


app = Flask(__name__)

app.register_blueprint(index_bp)
