ARG PYTHON_VERSION
FROM python:${PYTHON_VERSION}

WORKDIR /usr/src/app

RUN mkdir /var/lib/err
RUN pip install errbot errcron
ADD config.py ./
ADD demo.plug ./
ADD demo.py ./

CMD ["errbot", "-T"]
