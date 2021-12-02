FROM python:3.8.10
MAINTAINER Oleksandr Shevchenko <a6.shevchenko@itransition.com>

COPY . .
RUN pip install -r requirements.txt
# EXPOSE 5405
CMD ["python3","start.py"]
