from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class BadgeView(BrowserView):

    def __call__(self):
        """"""
        return "this is where the badge stuff shows up"