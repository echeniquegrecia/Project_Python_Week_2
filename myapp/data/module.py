from .browser import MyBrowser

__all__ = ['MyModule']

class MyModule():
    BROWSER = MyBrowser

    def __init__(self):
        self.BROWSER = self.BROWSER()