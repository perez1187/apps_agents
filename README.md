

wsgi.py and manage.py -> check local/prod

docker:
 docker build -t agents_api .
 docker run -p 8888:8000 agents_api