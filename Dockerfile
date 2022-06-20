FROM python:3.8.6

WORKDIR /app

COPY ./app/requirements.txt /app/requirements.txt
RUN pip install --upgrade -r requirements.txt

COPY ./app /app

CMD ["python", "-u", "bot.py"]
