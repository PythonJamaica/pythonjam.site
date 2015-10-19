Developer Quickstart
====================

Install the buildout
---------------------
::

   sudo apt-get install libxslt-dev libxml2-dev python-dev -y

Setup a virtualenv and run buildout (takes about 10 minutes)::

   virtualenv venv
   venv/bin/pip install -U setuptools
   venv/bin/python bootstrap-buildout.py
   bin/buildout


Install site data
------------------
After installing the buildout you will want to install the site with
some sample data.

To quickly achieve this, run the following command from within your buildout directory::

    bin/pulldevdata


Start the site
----------------
To start the site, run the following command::

   bin/instance fg

This will lauch the site on port 8080
