from flask import Blueprint, request, redirect, url_for
hello = Blueprint('hello', __name__, url_prefix='/')


@hello.route('/')
def index():
    name = request.args.get('name', 'World')
    # return f'Hello {name}!'
    return redirect(url_for('auth.login'))