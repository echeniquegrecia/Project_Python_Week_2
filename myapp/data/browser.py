from weboob.browser import PagesBrowser, URL
from .pages.pokemon import PokemonPage
from .pages.profile_pokemon import ProfilePokemon

class MyBrowser(PagesBrowser):
    BASEURL = 'https://www.pokebip.com'

    """
    Pages definition
    """
    pokemon = URL(r'/pokedex/pokemon$', PokemonPage)
    pokemon_profile = URL(r'/pokedex/pokemon/(?P<pokemon_name>.*)', ProfilePokemon)
    pokemon_type = URL(r'/pokedex/pokemon\?types=(?P<pokemon_type>.*)', PokemonPage)
    pokemon_generation = URL(r'/pokedex/pokemon\?generations=(?P<pokemon_generation>.*)', PokemonPage)
    
    #test
    poke_search = URL(r'/pokedex/pokemon\?(?P<query>.*)', PokemonPage)


    def show_pokemons(self):
        self.pokemon.go()

        return self.page.get_pokemons()    

    def get_profile_pokemon(self, name):
        self.pokemon_profile.go(pokemon_name=name)

        return self.page.get_profile()

    def type_pokemons(self, poke_type):
        self.pokemon_type.go(pokemon_type=poke_type)
        return self.page.get_pokemons()

    def generation_pokemons(self, poke_generation):
        self.pokemon_generation.go(pokemon_generation=poke_generation)
        return self.page.get_pokemons()

    
    #test
    def search(self, query):
        self.poke_search.go(query = query)
        return self.page.get_pokemons()




    