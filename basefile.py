from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login_user():
    return 'ok'


@app.route('/logout', methods=['GET'])
def logout_user():
    return 'ok'


@app.route('/register', methods=['GET', 'POST'])
def register_user():
    return 'ok'


@app.route('/user_page', methods=['GET'])
def user_access():
    return 'ok'


@app.route('/currency', methods=['GET', 'POST'])
def currency_converter():
    return 'ok'
