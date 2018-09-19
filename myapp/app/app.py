from flask import Flask, render_template

app = Flask(__name__, template_folder='views')



@app.route('/')
def hello():
    return 'Hello, World!'


from myapp.app.controllers import PokemonController
app.register_blueprint(PokemonController.bp)