import json

from weboob.browser import LoginBrowser, URL, need_login
from weboob.exceptions import BrowserIncorrectPassword

from .pages.home import HomePage
from .pages.login import LoginPage
from .pages.profile import ProfilePage


class MyBrowser(LoginBrowser):
    BASEURL = 'https://www.instagram.com'

    """
    Pages definition
    """
    homePage = URL(r'/$', HomePage)
    loginPage = URL(r'/accounts/login/ajax/', LoginPage)
    profile = URL(r'/graphql/query/\?query_hash=ae377d9f4a6592f068e61eff185cd73f$', ProfilePage)

    def do_login(self):
        self.homePage.go()

        token, ajax = self.page.get_user_form()

        form = {
            'username': self.username,
            'password': self.password,
            'queryParams': {}
        }

        try:
            self.loginPage.go(
                data=form,
                headers={
                    'x-csrftoken': token,
                    'x-instagram-ajax': ajax,
                    'x-requested-with': 'XMLHttpRequest'
                }
            )
        except:
            raise BrowserIncorrectPassword

    @need_login
    def get_profile(self):
        return self.profile.go().get_profile()

    @need_login
    def get_posts(self):
        return self.profile.go().get_feed()