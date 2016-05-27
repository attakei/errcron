FROM python:3.5

WORKDIR /usr/src/app

RUN pip install errbot
RUN mkdir /var/lib/err
ADD config.py ./
ADD demo.plug ./
ADD demo.py ./
RUN pip install errcron -i https://testpypi.python.org/pypi

CMD ["errbot", "-T"]
