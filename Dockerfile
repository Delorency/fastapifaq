FROM python:3.11.2

WORKDIR /app

RUN pip install pipenv

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./

RUN chmod +x entrypoint.sh

CMD ["sh", "./entrypoint.sh"]