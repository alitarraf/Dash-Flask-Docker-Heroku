# DASH-Flask-Docker-Heroku
Starter code to containerise a DASH Python Flask application using Docker and deploying it to Heroku

# Steps
- Create a simple DASH Flask Application
- Containerise the DASH Flask application using Docker and test locally
- Deploy the container to Heroku 

You can refer to the following article by @ksashok for more details in Flask
https://medium.com/@ashok7067/containerise-your-python-flask-using-docker-and-deploy-it-onto-heroku-a0b48d025e43


# Useful commands

- `docker build -t flask-heroku:latest .`
- `docker run -d -p 5000:5000 flask-heroku`
- `heroku container:login`
- `heroku create yourawesomeapp`
- `heroku container:push web --app yourawesomeapp`
- `heroku container:release web --app yourawesomeapp`
