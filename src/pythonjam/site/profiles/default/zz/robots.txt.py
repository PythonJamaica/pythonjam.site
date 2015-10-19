## Script (Python) "robots.txt"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
# Example code:

# Import a standard function, and get the HTML request and response objects.
from Products.PythonScripts.standard import html_quote
request = container.REQUEST
response =  request.response
if request.URL1 in ["http://pythonjam.org.jm","http://www.pythonjam.org.jm",
                     "https://pythonjam.org.jm","https://www.pythonjam.org.jm"]:
    return ""
return """User-agent: *
Disallow: /"""
