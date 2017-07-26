#!/usr/bin/env bash

# Notice we are making these calls against nginx
echo
echo "It should print returned plain text:"
curl -H "Accept: text/html" http://localhost:80/
echo
echo "It should print returned json"
curl -H "Accept: application/json" http://localhost:80/
echo
echo "It should print returned json with key 'foo' and value 'xyz'"
curl -X POST -H "Content-Type: application/json" -X POST -d '{"foo":"xyz"}'  http://localhost:80/
echo
echo "If server is running with SERVER_MODE set as truthy value, then it should be greped here:"
# docker-compose has standard container naming so this container should be named dockerizedflaskdemo_app_1
docker exec dockerizedflaskdemo_app_1 cat /app/plangrid.log | grep xyz
