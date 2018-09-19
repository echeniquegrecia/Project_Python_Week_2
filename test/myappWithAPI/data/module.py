from .browser import MyBrowser

__all__ = ['MyModule']

class MyModule(object):
    BROWSER = MyBrowser

    def __init__(self, username, password):
        self.BROWSER = self.BROWSER(username, password)