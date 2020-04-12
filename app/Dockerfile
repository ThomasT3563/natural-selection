FROM python:3.8.0-alpine

WORKDIR /usr/src/app

RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

# run script
CMD [ "python", "foo.py"]
