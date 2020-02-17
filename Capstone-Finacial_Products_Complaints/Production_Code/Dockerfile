FROM ecoron/python36-sklearn:latest

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python"]

EXPOSE 5000

CMD ["flask_app.py"]