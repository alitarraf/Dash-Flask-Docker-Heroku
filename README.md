# DASH-Flask-Docker-Heroku
Starter code to containerise a DASH Python Flask application using Docker and deploying it to Heroku

# Steps
- Create a simple DASH Flask Application
- Containerise the DASH Flask application using Docker and test locally
- Deploy the container to Heroku 

You can refer to the following article by @ksashok for more details in Flask
https://medium.com/@ashok7067/containerise-your-python-flask-using-docker-and-deploy-it-onto-heroku-a0b48d025e43


## Step by step commands

1. `docker build -t flask-heroku:latest .`
2. `docker run -d -p 5000:5000 flask-heroku`
3. `heroku container:login`
4. `heroku create yourawesomeapp`
5. `heroku container:push web --app yourawesomeapp`
6. `heroku container:release web --app yourawesomeapp`

# Docker-Compose - how to push multiple docker images under one heroku app?
For a directory structure should look something like this with dockerfiles named with an extension 'Dockerfile.<process-type>' as per this [link](https://devcenter.heroku.com/articles/container-registry-and-runtime).  

```
app  
|---docker-compose.yml  
|---one  
|------one\dockerfile.one  
|------one\appone.py  
|---two  
|------two\dockerfile.two  
|------two\apptwo.py  
```
  
You should replace step 5 in the steps above by a recursive call for heroku to look into each one of the dockerfile recursively.
`heroku container:push --app <yourappname> --recursive`

After that release your web app as per step 6.

