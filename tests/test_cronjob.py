from datetime import datetime
from errcron.cronjob import CronJob


def test_for_display():
    job = CronJob()
    job.set_triggers('%H', '01')
    assert str(job) == 'CronJob(trigger=[%H->01])'
    job = CronJob()
    assert str(job) == 'CronJob(trigger=[])'


def test_not_run_in_target_time():
    job = CronJob()
    job.trigger_format = '%H'
    job.trigger_time = '01'
    dt = datetime(2000, 1, 1, 1, 1, 1)
    assert job.is_runnable(dt) is True
    dt = datetime(2000, 1, 1, 0, 1, 1)
    assert job.is_runnable(dt) is False


def test_set_triggers():
    job = CronJob()
    job.set_triggers('%H', '01')
    dt = datetime(2000, 1, 1, 1, 1, 1)
    assert job.is_runnable(dt) is True
    dt = datetime(2000, 1, 1, 0, 1, 1)
    assert job.is_runnable(dt) is False
