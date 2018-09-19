import re
from myapp.app.models.pokemon import Pokemon
from weboob.browser.pages import HTMLPage
from weboob.capabilities.base import BaseObject, Field, StringField, IntField
from weboob.browser.elements import TableElement, ItemElement, method
from weboob.browser.filters.standard import CleanText, CleanDecimal, TableCell
from weboob.browser.filters.html import Attr

class ProfilePokemon(HTMLPage):
    @method
    class get_profile(ItemElement):
        klass = Pokemon

        obj_pv = CleanDecimal('//div[contains(., "Aper")]/following-sibling::table//tr[2]/td[2]')
        obj_attaque = CleanDecimal('//div[contains(., "Aper")]/following-sibling::table//tr[3]/td[2]')
        obj_image = CleanText('//div[contains(@class, "text")]/img/@src')