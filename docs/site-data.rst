====================
pythonjam.site
====================

Releasing Site Data
---------------------
The PythonJamaica site is for public consumption, and so we occasionally release the data needed to rebuild the site
to the public.

We realize that publishing data that may include user data may be problematic. To mitigate against this we first
"defang" the data by removing all user data before releasing it.

::

    bin/sanitize

The sanitized version of the data is located in a folder of your buildout called `sanitized`.

It should be safe to share the resulting file with other developers: sanitized/pythonjam.site.data.tar.gz

Retrieving the Site Data
---------------------------
A version of the sanitized data can be retrieved automatically using the following command from within your buildout::

    bin/pulldevdata


