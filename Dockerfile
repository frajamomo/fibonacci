FROM python:latest
LABEL Maintainer='frajamomo'

WORKDIR ./

COPY *.py ./ 

CMD [ "python", "-m", "unittest", "--verbose"]