import six


def echo_hello():
    pass


def echo_datetime(plugin, polled_time):
    return polled_time.strftime('%Y-%m-%d')


def echo_datetime_with_head(plugin, polled_time, prefix):
    return prefix + polled_time.strftime('%Y-%m-%d')


def print_datetime(plugin, polled_time):
    six.print_(polled_time.strftime('%Y-%m-%d'), end='')


def print_datetime_with_str(plugin, polled_time, prefix):
    six.print_(prefix + polled_time.strftime('%Y-%m-%d'), end='')
