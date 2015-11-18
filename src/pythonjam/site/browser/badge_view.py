from Products.Five import BrowserView


class BadgeView(BrowserView):

    def __call__(self):
        """"""
        return "this is where the badge stuff shows up"
