## Script (Python) "invite_to_slack"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
import DateTime
dt = DateTime.DateTime()
timestamp = int(dt.timeTime())

postdata = """email:example@example.com
channels:C02RWGV3X,C02S05WJA,C02SU0WLE,C02S2B5CH,C02RVB0CK,C02SPEMBY
first_name:Example
token:xoxs-255168432
set_active:true
_attempts:1"""

url = "https://pythonjam.slack.com/api/users.admin.invite?t={}".format(timestamp)
return url
