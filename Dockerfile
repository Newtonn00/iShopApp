FROM python:3.9.16-slim
RUN mkdir /var/app
RUN mkdir /var/app/ishop
WORKDIR /var/app/ishop
ARG WORKDIR=/var/app/ishop
ENV WORKDIR="${WORKDIR}"
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
ENV PYTHONPATH "/var/app/ishop"
CMD ["python3","/var/app/ishop/src/controller/main.py"]
