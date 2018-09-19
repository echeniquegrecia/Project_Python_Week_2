from flask import Flask, Blueprint, render_template,request, redirect
from myapp.data.browser import MyBrowser
from urllib.parse import urlencode
bp = Blueprint('PokemonController', __name__)

browser = MyBrowser()

@bp.route('/all/pokemons')
def all_pokemons():
    return render_template('pokemons.html', arguments={'pokemons':browser.show_pokemons()})

@bp.route('/pokemons/<pokemon>')
def get_profile_pokemon(pokemon):
    return render_template('pokemons_profile.html', arguments={'pokemon_name':pokemon, 'pokemons':browser.show_pokemons(), 'profile':browser.get_profile_pokemon(pokemon)})

@bp.route('/find/pokemons/', methods=('GET', 'POST'))
def find_pokemons():
    if request.method == 'POST':
        type_poke = request.form.getlist('type_poke')
        generation = request.form.getlist('generation')
        if not type_poke and not generation and not talent:
            return redirect('/find/pokemons/')
        else:
            if type_poke and not generation:
                data={'types': ",".join(str(x) for x in type_poke)}
                query=urlencode(data)
                return redirect('/find/pokemons/by/'+ str(query))
            elif generation and not type_poke:
                data={'generations':",".join(str(x) for x in generation)}   
                query=urlencode(data)
                return redirect('/find/pokemons/by/'+ str(query))

            data={'types': ",".join(str(x) for x in type_poke), 'generations':",".join(str(x) for x in generation)}
            query=urlencode(data)
            return redirect('/find/pokemons/by/'+ str(query))
               
    return render_template('pokemons_find.html')


@bp.route('/find/pokemons/by/<query>')
def find_type(query):
    return render_template('pokemons_find_result.html', arguments={'pokemons':browser.search(query)})