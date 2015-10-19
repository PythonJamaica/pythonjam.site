==============================================================================
The PythonJamaica Site
==============================================================================

This is the code for the PythonJamaica website

It is used to power http://pythonjam.org.jm

Documentation
-------------

Full documentation for end users can be found in the "docs" folder, and is also available online at http://pythonjamaica-website.readthedocs.org/


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
   bin/pulldevdata

Starting the site
~~~~~~~~~~~~~~~~~~~

To start the site, run the following command::

   bin/instance fg

This will launch the site, once you see "INFO Zope Ready to handle requests"

From the IDE click 1) "Preview running app" and 2) click to "pop out in a new windows"

.. image:: https://github.com/PythonJamaica/pythonjam.site/blob/master/docs/previewrunningapp.png

Then click preview 

.. image:: https://github.com/PythonJamaica/pythonjam.site/blob/master/docs/clicktopreview.png

Contribute
----------

- Issue Tracker: https://github.com/PythonJamaica/pythonjam.site/issues
- Source Code: https://github.com/PythonJamaica/pythonjam.site
- Documentation: http://pythonjamaica-website.readthedocs.org/


Support
-------

If you are having issues, please let us know.
Use the contact information at http://pythonjam.org.jm


License
-------

The project is licensed under the GPLv2.
