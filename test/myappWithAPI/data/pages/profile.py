from weboob.browser.pages import JsonPage
from weboob.capabilities.profile import Profile
from weboob.browser.elements import method, ItemElement, DictElement
from weboob.browser.filters.standard import CleanText
from weboob.browser.filters.json import Dict
from weboob.capabilities.base import (
    BaseObject, Field, StringField, IntField
)

class Post(BaseObject):
    name = StringField('Name')
    username = StringField('Username')
    picture = StringField('Picture')

class ProfilePage(JsonPage):
    @method
    class get_profile(ItemElement):
        klass = Profile

        obj_name = Dict('data/user/username')
        obj__picture = Dict('data/user/profile_pic_url')

    @method
    class get_feed(DictElement):
        item_xpath = 'data/user/edge_web_feed_timeline/edges'

        def find_elements(self):
            for part in super().find_elements():
                yield part.get('node')

        class item(ItemElement):
            klass = Post

            obj_name = Dict('owner/full_name')
            obj_username = Dict('owner/username')
            obj_picture = Dict('display_url')