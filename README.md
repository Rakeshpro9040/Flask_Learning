# Key URLs
https://github.com/tecladocode/rest-apis-flask-python/tree/develop/project
https://blog.teclado.com/python-dictionary-merge-update-operators/

# Docker Build
docker build -t rest-apis-flask-python .
docker build -t flask-smorest-api . 
- Here t is the tag

# Run container with existing code
docker run -dp 5005:5000 rest-apis-flask-python
docker run -dp 5005:5000 flask-smorest-api
- Here d = run as daemon/background; p = port
- 5005 = local machine port; 5000 = docker container port

# Run container with volume (host folder synxed with container folder)
docker run -dp 5005:5000 -w /app -v "$(pwd):/app" flask-smorest-api
- Here w = replace the container /app with host folder 
- v = is to create mapping bet $(pwd) ie host folder to /app ie container folder

# Browse swagger-ui
http://localhost:5005/swagger-ui

# marshmallow
- Here dump_only indicates that skip for validation, will be used while sending data back
- Required indicates that validations is needed or not for this field
- Note that while sending back data to client both dump_only & required fields are manadatory*
- Note that while receiving data from client only required fields are manadatory*
- Marshmallow can convert dictionary/object into JSON, so can easily integrate 
- arguments decorator is for client input validation, post validation it will return a JSON
- response decorator is for sending the response to client as JSON with validated schema
