==================================================
Koding.io Ansible playbook for PythonJam.org.jm
==================================================

.. admonition:: Description

    Use Ansible to provision a full-stack Plone server


Introduction
------------

This Ansible Playbook is used to test provisioning to a koding.io based Virtual machine.

To use you must do the following
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Install a working version of Ansible locally

2. Install shared keys on your koding.io VM

3. Run ``ansible-galaxy -p roles -r requirements.txt install`` to install required roles;

4. Edit ``local-configure.yml`` and add a plone password and admin email

5. To deploy edit ``myhost.cfg`` to match your koding.io VM then run, ``ansible-playbook -i myhost.cfg playbook.yml``;


.. warning::

    This version of the playbook requires that the plone.plone_server role be 1.2.0+.
