def echo_hello():
    pass


def echo_datetime(polled_time):
    return polled_time.strftime('%Y-%m-%d')


def echo_datetime_with_head(polled_time, prefix):
    return prefix + polled_time.strftime('%Y-%m-%d')
