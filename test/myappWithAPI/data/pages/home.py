import re

from weboob.browser.pages import HTMLPage
from weboob.browser.filters.standard import CleanText

class HomePage(HTMLPage):
    def get_user_form(self):
        token = re.search(r'"csrf_token":"(.*?)"', self.text).group(1)
        ajax = re.search(r'"rollout_hash":"(.*?)"', self.text).group(1)
        
        return (token, ajax)

