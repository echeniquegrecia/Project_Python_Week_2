import re

from app.models.pokemon import Pokemon

from weboob.browser.pages import HTMLPage
from weboob.browser.elements import TableElement, ItemElement, method
from weboob.browser.filters.standard import CleanText, CleanDecimal, TableCell
from weboob.browser.filters.html import Attr


class PokemonPage(HTMLPage):
    @method
    class get_pokemons(TableElement):
        item_xpath = '//table[contains(@class, "table")]//tr[td]'
        head_xpath = '//table[contains(@class, "table")]//th'

        col_id = re.compile('#')
        col_name = re.compile('Nom')
        col_type = re.compile('Type')
        col_num = re.compile('Numéro')

        class item(ItemElement):
            klass = Pokemon

            obj_id = CleanDecimal('td[1]')
            obj_pokedex_id = obj_id
            
            def obj_type(self):
                types = []

                for type in TableCell('type')(self)[0].xpath('./div'):
                    types.append(Attr('.//img', 'alt')(type))

                return types
            
            def obj_name(self):
                return CleanText(TableCell('name')(self)[0].xpath('./strong/a/text()'))(self)
