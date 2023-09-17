https://github.com/tecladocode/rest-apis-flask-python/tree/develop/project

docker build -t rest-apis-flask-python .
- Here t is the tag

docker run -dp 5005:5000 rest-apis-flask-python
- Here d = run as daemon/background; p = port
- 5005 = local machine port; 5000 = docker container port