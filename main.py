from flask import request, make_response, redirect, render_template, session, url_for, flash
import unittest
from app import create_app
from app.forms import LoginForm
from app.databse import get_users, get_alls

app = create_app()


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)


@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip

    return response


@app.route('/hello', methods=['GET'])
def hello():
    user_ip = session.get('user_ip')
    username = session.get('username')
    context = {
        'user_ip': user_ip,
        'alls': get_alls(username=username)[0],
        'username': username,
    }

    return render_template('hello.html', **context)
