Crontab implementation for Errbot
=================================

It is extention for plugin of Errbot to implement poller llike crontab.

Requirements
------------

* Python 2.7, 3.4 or 3.5
* `six <https://pypi.python.org/pypi/six>`_
* `crontab <https://pypi.python.org/pypi/python-crontab>`_
* `pytz <https://pypi.python.org/pypi/pytz>`_
* `(Errbot) <https://pypi.python.org/pypi/Errbot>`_


Installation
------------

.. code-block::

   $ pip install errcron
   or
   $ pip install git+https://github.com/attakei/errcron.git


Usage
-----

Example
^^^^^^^

.. code-block:: python

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


Changes
-------

version 0.4.1
^^^^^^^^^^^^^

* Fix missing dependencies

version 0.4
^^^^^^^^^^^

* Enable class TIMEZONE definition
* Set order of extends


License
-------

Errbot is available as open source software and released under the GPL v3 license.

See `full license file <./LICENSE>`_.
