FROM python:2.7

WORKDIR /usr/src/app

RUN pip install errbot
RUN mkdir /var/lib/err
ADD config.py ./
ADD demo.plug ./
ADD demo.py ./
RUN pip install errcron

CMD ["errbot", "-T"]
