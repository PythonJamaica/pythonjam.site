from plone import api
import transaction

for user in api.user.get_users():
    print "zapping %s" % user.id
    api.user.delete(user=user)
transaction.commit()
