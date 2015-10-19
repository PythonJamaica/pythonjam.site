import transaction
import os
HOSTNAME = os.getenv('C9_HOSTNAME',None)
if HOSTNAME:
    app.virtual_hosting.set_map('{0}/VirtualHostBase/https/{0}/pythonjam'.format(HOSTNAME))
transaction.commit()
