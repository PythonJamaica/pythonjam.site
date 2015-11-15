====================
Managing Site Data
====================

The PythonJamaica site is for public consumption, and so we occasionally release the data needed to rebuild the site
to the public. 
Before releasing the data we remove all member data from the database.

These are notes related making use of this site data during development and how to package and release
new site data.


Retrieving the Site Data
---------------------------

A version of the sanitized data can be retrieved automatically using the following command from within your buildout::

   bin/pulldevdata


Releasing Site Data
---------------------

.. important:: This task should be executed on a slave copy of the production system.

The goal is to create a snapshot of real data that developers can
work with without needing to disturb the live site.

We are careful not to publish any data of our site users. To achieve this we
"defang" the site data by removing all user account data before releasing it.

::

    bin/sanitize

The sanitized version of the data is located in a folder of your buildout called `sanitized`.

It should be safe to share the resulting file with other developers: sanitized/pythonjam.site.data.tar.gz

To release the latest data
`````````````````````````````````

* Upload the snapshot to https://github.com/PythonJamaica/pythonjam.site/releases
* Update the link in templates/pulldevdata.in

