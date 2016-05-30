FROM python:2.7

WORKDIR /usr/src/app

RUN pip install errbot crontab
RUN mkdir /var/lib/err
RUN pip install errcron -i https://testpypi.python.org/pypi
ADD config.py ./
ADD demo.plug ./
ADD demo.py ./

CMD ["errbot", "-T"]
