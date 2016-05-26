FROM python:2.7

WORKDIR /usr/src/app

RUN pip install errbot
ADD config.py ./
RUN mkdir /var/lib/err
RUN pip install errcron -i https://testpypi.python.org/pypi

CMD ["errbot", "-T"]
