.. highlight:: shell

============
Installation
============


Stable release
--------------

To install ISLEX pronunciation dictionary core entries, run this
command in your terminal:

.. code-block:: console

    $ pip install islex-core

This is the preferred method to install the core data entries, as it
will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


From sources
------------

The sources for ISLEX pronunciation dictionary core entries can be
downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/jkahn/islex-core

Or download the `tarball`_:

.. code-block:: console

    $ curl  -OL https://github.com/jkahn/islex-core/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py bdist_wheel
    $ pip install -U dist/*.whl


.. _Github repo: https://github.com/jkahn/islex-core
.. _tarball: https://github.com/jkahn/islex-core/tarball/master


Release checklist
-----------------

Update HISTORY.rst with release notes for *upcoming* release.
Commit to master.
  
Check that everything still works:

.. code-block:: console

    $ make test-all

Update the version number:

.. code-block:: console

    $ bumpversion patch  # or minor, or major?

Make sure everything still works:

.. code-block:: console

    $ make test-all
    
Push the version bump and its tag up to the repo:

.. code-block:: console

    $ git push; git push --tags
    
Expect (if you're Jeremy) that travis will push the wheel to pypi.

Edit the release on Github
(e.g. https://github.com/jkahn/islex/releases). Paste release notes
into the release's release page, and come up with a title for the
release.
