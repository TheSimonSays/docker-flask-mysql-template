from flask import jsonify
from app.routes.main import bp


@bp.route('/', methods=['GET', 'POST'])
def index():
    return jsonify({'response': 'ok'})
    