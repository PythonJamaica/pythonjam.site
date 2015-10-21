==============================================================================
The PythonJamaica Site
==============================================================================

This is the code for the PythonJamaica website

It is used to power http://pythonjam.org.jm

Documentation
-------------

Full documentation is available online at http://pythonjamaica-website.readthedocs.org/


Development
------------

To get started with development we recommend using Cloud9 IDE

Start by creating a workspace (the default is fine).

Create a new workspace and under "Clone from Git" use the following git repo URL
https://github.com/PythonJamaica/pythonjam.site.git

.. image:: https://github.com/PythonJamaica/pythonjam.site/blob/master/docs/createnewworkspace.png

Then run the following commands in a terminal::

   sudo apt-get install libxslt-dev libxml2-dev -y

Setup a virtualenv and run buildout (takes about 10 minutes)::

   virtualenv venv
   venv/bin/python bootstrap-buildout.py
   bin/buildout
   
You may need to run "bin/buildout" again if it breaks or fails the first time.
Then pull the site data and setup https::

   bin/pulldevdata
   bin/setuphttps

Starting the site
~~~~~~~~~~~~~~~~~~~

To start the site, run the following command::

   bin/instance fg

This will launch the site, once you see "INFO Zope Ready to handle requests"

From the IDE click 1) "Preview running app" and 2) click to "pop out in a new window"

.. image:: https://github.com/PythonJamaica/pythonjam.site/blob/master/docs/previewrunningapp.png


You can now to view your Plone site. This will reveal a working copy of the PythonJamaica site.

.. image:: https://github.com/PythonJamaica/pythonjam.site/blob/master/docs/clicktopreview.png

Logging in
~~~~~~~~~~~~~~~

You can login by visiting /login and using the following credentials::

    username: admin
    password: admin


Contribute
----------

- Issue Tracker: https://github.com/PythonJamaica/pythonjam.site/issues
- Source Code: https://github.com/PythonJamaica/pythonjam.site
- Documentation: http://pythonjamaica-website.readthedocs.org/


Support
-------

Please report any problems using our Issue Tracker: https://github.com/PythonJamaica/pythonjam.site/issues

Then alert us via any of our community channels mentioned at http://pythonjam.org.jm/join


License
-------

The project is licensed under the GPLv2.
