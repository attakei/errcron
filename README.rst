Crontab implementation for Errbot
=================================

It is extention for plugin of Errbot to implement poller llike crontab.

Requirements
------------

* Python 2.7,3.4 or 3.5
* `six <https://pypi.python.org/pypi/six>`_
* `crontab <https://pypi.python.org/pypi/crontab>`_
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

   class ClockTimer(BotPlugin, CrontabMixin):
       CRONTAB = [
           '@hourly .post_hourly',
           '0 8 * * * .post_morning_call @attakei'
       ]

       def activate(self):
           super(Crontab, self).activate()
           self.activate_crontab()

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

version 0.3
^^^^^^^^^^^

* Implement crontab format.
* Implement be able to run instance method of plugin.
* Change plling interval


License
-------

Errbot is available as open source software and released under the GPL v3 license.

See `full license file <./LICENSE>`_.
