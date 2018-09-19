from weboob.capabilities.base import (
    BaseObject, Field, StringField, IntField, DecimalField
)


class Pokemon(BaseObject):
    pokedex_id = IntField('Pokedex id of the Pokemon')
    name = StringField('Name of the Pokemon')
    types = Field('Types of the Pokemon')
    pv = DecimalField('PV of the Pokemon')
    attaque = DecimalField('Attaque of the Pokemon')
    image = StringField('Image of the Pokemon')