Crontab implementation for Errbot
=================================

It is extention for plugin of Errbot to implement poller llike crontab.

.. image:: https://img.shields.io/pypi/v/errcron.svg
   :target: https://pypi.org/project/errcron/
   :alt: Version in PyPI

.. image:: https://img.shields.io/pypi/pyversions/errcron.svg
   :target: https://pypi.org/project/errcron/
   :alt: python versions

.. image:: https://img.shields.io/pypi/l/errcron.svg
   :target: https://pypi.org/project/errcron/
   :alt: License

.. image:: https://requires.io/github/attakei/errcron/requirements.svg?branch=master
   :target: https://requires.io/github/attakei/errcron/requirements/?branch=master
   :alt: Requirements Status


Requirements
------------

* Python 2.7 or 3.4+
* `six <https://pypi.python.org/pypi/six>`_
* `crontab <https://pypi.python.org/pypi/python-crontab>`_
* `pytz <https://pypi.python.org/pypi/pytz>`_
* `(Errbot) <https://pypi.python.org/pypi/Errbot>`_


Installation
------------

.. code-block:: bash

   $ pip install errcron
   or
   $ pip install git+https://github.com/attakei/errcron.git


Usage
-----

Example
^^^^^^^

.. code-block:: python

   from errcron import CrontabMixin


   class ClockTimer(CrontabMixin, BotPlugin):
       CRONTAB = [
           '@hourly .post_hourly',
           '0 8 * * * .post_morning_call @attakei'
       ]

       def activate(self):
           super().activate()
           # some expression

       def post_hourly(self, polled_time):
           user =  self.build_identifier('#general')
           return self.send(user, 'Just {} o-clock!!'.format(polled_time.strftime('%H')))

       def post_morning_call(self, polled_time, identity):
           user =  self.build_identifier(identity)
           return self.send(user, 'Good morning!')

#. Extend your plugin by CrontabMixin
#. Define crontab
#. In activate, activate crontab too
#. Run


Latest changes
--------------

version 0.4.4
^^^^^^^^^^^^^

* Fix for latest crontab-parser
* Fix test targets in Travis-CI

version 0.4.3
^^^^^^^^^^^^^

* Add python 3.6 for test target (compatible)
* Can import as ``from errcron import CrontabMixin``


License
-------

Errbot is available as open source software and released under the GPL v3 license.

See `full license file <./LICENSE>`_.
