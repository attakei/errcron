Crontab implementation for Errbot
=================================

Requirements
------------

* Python 2.7,3.4 or 3.5
* Errbot


Installation
------------

.. code-block::

   $ pip install errcron
   or
   $ pip install git+https://github.com/attakei/errcron.git


Usage
-----

1. Extend your plugin by CrontabMixin and activate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   class Crontab(BotPlugin, CrontabMixin):
       CRONTAB = [
           '%H 12 errcron.action.post_message #general LunchTime!',
       ]

       def activate(self):
           super(Crontab, self).activate()
           self.activate_crontab()

2. Define your crontab
^^^^^^^^^^^^^^^^^^^^^^

3. Run
^^^^^^


License
-------

Errbot is available as open source software and released under the GPL v3 license.

See `full license file <./LICENSE>`_.
