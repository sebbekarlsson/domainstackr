from flask import Blueprint, render_template, abort, request, redirect, session


bp = Blueprint(
    __name__, __name__,
    template_folder='templates'
)

@bp.route('/', methods=['POST', 'GET'])
def render():
    return render_template('index.html')
