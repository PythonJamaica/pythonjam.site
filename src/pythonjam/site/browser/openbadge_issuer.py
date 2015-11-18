import json
from Products.Five import BrowserView

class OpenBadgeIssuerJSON(BrowserView):

    def __call__(self):
        """"""
        issuer = json.dumps({'name': 'Python Jamaica',
                             'url': 'http://www.pythonjam.org.jm',
                             'description': 'PythonJamaica website',
                             'email': 'admin@pythonjam.org.jm'})
        return issuer