from weboob.capabilities.base import (
    BaseObject, Field, StringField, IntField
)

class Pokemon(BaseObject):
    pokedex_id = IntField('Pokedex id of the Pokemon')
    name = StringField('Name of the Pokemon')
    types = Field('Types of the Pokemon')