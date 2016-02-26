pytest-platform-markers
===================================

.. image:: https://travis-ci.org/The-Compiler/pytest-platform-markers.svg?branch=master
    :target: https://travis-ci.org/The-Compiler/pytest-platform-markers
    :alt: See Build Status on Travis CI

.. image:: https://ci.appveyor.com/api/projects/status/github/The-Compiler/pytest-platform-markers?branch=master
    :target: https://ci.appveyor.com/project/The-Compiler/pytest-platform-markers/branch/master
    :alt: See Build Status on AppVeyor

Markers for pytest to skip tests on specific platforms

----

Features
--------

This plugin adds the following markers to pytest:

* ``posix``: Skipped except on a POSIX os (Linux/OS X, ``os.name != 'posix'``)
* ``windows``: Skipped except on Windows (``os.name != 'nt'``)
* ``linux``: Skipped except on Linux (``sys.platform.startswith('linux')``)
* ``osx``: Skipped except on OS X (``sys.platform != 'darwin'``)
* ``not_osx``: Skipped on OS X (``sys.platform == 'darwin'``)
* ``not_frozen``: Skipped when frozen (``getattr(sys, 'frozen', False)``)
* ``frozen``: Skipped except when frozen (``not getattr(sys, 'frozen', False)``)
* ``ci``: Skipped except on CI systems (``'CI' not in os.environ``)
* ``not_ci``: Skipped on CI systems (``'CI' in os.environ``)

Installation
------------

You can install "`pytest-platform-markers`_" via `pip`_ from `PyPI`_::

    $ pip install pytest-platform-markers


Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the `MIT`_ license, "pytest-platform-markers" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`MIT`: http://opensource.org/licenses/MIT
.. _`BSD-3`: http://opensource.org/licenses/BSD-3-Clause
.. _`GNU GPL v3.0`: http://www.gnu.org/licenses/gpl-3.0.txt
.. _`Apache Software License 2.0`: http://www.apache.org/licenses/LICENSE-2.0
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/The-Compiler/pytest-platform-markers/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.org/en/latest/
.. _`pip`: https://pypi.python.org/pypi/pip/
.. _`PyPI`: https://pypi.python.org/pypi
.. _`pytest-platform-markers`: https://pypi.python.org/pypi/pytest-platform-markers
