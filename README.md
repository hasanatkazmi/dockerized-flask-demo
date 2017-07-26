# Dockerized Flask Demo

We use `docker-compose` to launch two containers: flask app exposed behing `wsgi` server (`app`) and nginx reverse proxy (`nginx`).

`nginx` is exposed at port 80 and `wsgi` is being 8080.

## The app:
We have a basic flask app which exposes one end point (```"/"```) that accepts both ```GET``` and ```POST```.
If ```Accept``` header is set as ```text/html```, then ```<p>Hello, World</p>``` is returned. If its set as ```application/json``` then json ```{"message": "Good morning"}``` is returned.
Furthermore, while processing ```POST```, if server finds ```SERVER_MODE``` environment variable set as truth (1, True, true etc), then this request is logged in ```plaingrid.log``` in ```/app``` directory.

## Tests:
Within `app`, we have `test-unit.py` that have unit tests for the app. You may run `python test-unit.py` to run all units tests (by mocking endpoints). We also have `./test-smoke` that uses curl to fetch data from endpoint and prints to stdout. You can only use `./test-smoke` when we have containers running.

## How to:
Run these commands:
```
git clone https://github.com/hasanatkazmi/dockerized-flask-demo.git
cd dockerized-flask-demo
docker-compose build
docker-compose up
```

Now run `./test-smoke` in `app` directory to see if things are running correctly.

You can modify `app/Dockerfile` and remove `ENV SERVER_MODE=1` and build and run containers again and run smoke test again to ensure that logging functionality is also working as intended.
