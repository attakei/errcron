Sample usage
============

Simply usage
------------

.. code-block:: python

   from errbot import BotPlugin
   from errcron.bot import CrontabMixin


   class Crontab(BotPlugin, CrontabMixin):
       CRONTAB = [
           '0 8 * * * .post_morning_call'
       ]

       def activate(self):
           super().activate()
           self.activate_crontab()

       def morning_meeting(self, polled_time):
           user =  self.build_identifier('#general')
           return self.send(user, 'Just {} o-clock!!'.format(polled_time.strftime('%H')))

#. Using crontab bot plugin must be extended by CrontabMixin.
   And call ``activate_crontab`` in activation plugin.
#. Define schedule and job as like as crontab in ``CRONTAB`` property in bot-plugin class.
#. Cronjob function has least one arguments.
   ``polled_time`` is datetime instance of time called in function.


Crontab scheduling
------------------

errcron use crontab like job scheduliing.
See `crontab page in PyPI`_

.. _crontab page in PyPI: https://launchpad.net/python-crontab