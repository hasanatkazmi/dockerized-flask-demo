
FROM ubuntu

RUN apt-get update
RUN apt-get install -y vim dialog net-tools curl python-pip python-dev build-essential
RUN pip install --upgrade pip

EXPOSE 8080

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
# Remove SERVER_MODE var, run the container again and run smoke test to ensure its working as required.
ENV SERVER_MODE=1
ENTRYPOINT ["python"]
CMD ["main.py"]

