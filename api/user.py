from flask import Blueprint

user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/t')
def hello_world():
    return 'user!'
