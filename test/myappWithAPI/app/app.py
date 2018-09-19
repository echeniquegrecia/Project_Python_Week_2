from flask import (
    Flask, request, flash, redirect, render_template, url_for,
)
from wtforms import (
    Form, BooleanField, StringField, PasswordField, validators,
)
from data.module import MyModule as Insta
from weboob.exceptions import BrowserIncorrectPassword

app = Flask(__name__, template_folder='views')
MyModule = None

@app.route('/')
def hello():
    return 'Hello, World!'

class LoginForm(Form):
    username = StringField('Username', [])
    password = PasswordField('Password', [])

@app.route('/profile')
def profile():
    print(MyModule)
    return render_template('profile.html', user={'username': "test"})

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        MyModule = Insta(request.form.get('username'), request.form.get('password'))
        try:
            return render_template('profile.html', user=MyModule.BROWSER.get_profile(), feed=MyModule.BROWSER.get_posts())
        except Exception as e:
            print(e)
            print('Mauvaises informations')
    return render_template('login.html', form=form)