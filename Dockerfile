FROM python:3.9.16-slim
RUN mkdir /var/app
RUN mkdir /var/app/ishop
WORKDIR /var/app/ishop
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN ls -la

EXPOSE 5000

CMD ["ls"]
CMD ["flask","--app","./controller/main.py","run"]
