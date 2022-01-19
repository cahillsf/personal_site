## TO DO
- debounce window resize event listener
- make sure DD instrumentation works
  * passing in RUM envvars to Vue -in k8s
  * ~~copy in custom style sheet~~
- containerize 
  * ~generate images for kube deployment~

- style
  * fix up dropdown menu
  * add breakpoint for large screens (increase grid-row gap?  maybe add some rows?)-- so bottom bar is always at bottom -- maybe there's an easier fix here....

- production build
  * updating all sensitive info for config -- MongodDB users/pws/access, flask userrole and pword -- as envvars
  * writing kube yaml deployment
- go live


* ~~better routing--> can i create a router-link within a different element?~~

* ~~styling-- figure out a way to keep theming (currently in nodemodules which are in the .gitignore)~~

* ~~hide dropdown menu after user has returned to full page view so that when the browser size is reduced below the breakpoint, it will not be visible~~


# Theme
* default UIkit theme is in node_modules/@vuikit/theme/dist/vuikit.css


## Git 
* add remote repo to track origin
`
git remote add origin https://github.com/cahillsf/funvue-project.git
git branch -M main
git push -u origin main
`
docker build -t ps-vue .

docker image tag ps-vue cahillsf/ps-vue:0.0.1
docker image push cahillsf/ps-vue:0.0.1


## Flask App
from /Users/scahill/Desktop/funvue-project/flask-server
- activate virtual environment: `source .venv/bin/activate`

run the app:
- python app.py
- ddtrace-run python app.py

to get idle: `idle` from terminal

https://github.com/tensorflow/tensorboard/issues/1566

## Mongodb 
cd docker-entrypoint-initdb.d


mongoimport -u "root" -p "example" --type csv --authenticationDatabase admin -d sitecontent -c cards --headerline homepage.csv

./mongo-db/mongo-db-init-files
* mongo -uroot -pexample

from the container bash: `mongosh --username root --password example --authenticationDatabase admin`

`mongosh --username flask-role --password toor --authenticationDatabase sitecontent`

db.serverStatus().connections

use sitecontent
var col = db.cards
col.find()


#  db.getCollection('cards').find()

use sitecontent
db.createCollection('cards')
var myCards=
	[
		{
            '_id': 0,
            'title':'CardOne',
            'msg':'testOne',
            'animation':'fade-up'
          },
          {
            '_id': 1,
            'title':'CardTwo',
            'msg':'testTwo',
            'animation':'fade-up'
          },
          {
            '_id': 2,
            'title':'CardThree',
            'msg':'testTwo',
            'animation':'fade-up'
          },
          {
            '_id': 3,
            'title':'CardFour',
            'msg':'testTwo',
            'animation':'fade-up'
          },

	];

	db.cards.insert(myCards);




## Minikube

* minikube service --url ps-vue-service


Building a local image and pushing to your Docker Hub registry is very straightforward if you have an image you'd like to make public
Build the image locally: in your terminal, navigate to the directory containing your Dockerfile, then run the following command: `docker build -t <IMAGE_NAME> .`
Tag the image with the following command: `docker image tag <IMAGE_NAME> <DOCKER_USERNAME>/<IMAGE_NAME>:<TAG>`
Push the image to your Docker Hub using the following command: `docker image push <DOCKER_USERNAME>/<IMAGE_NAME>:<TAG>`
Log in to Docker Hub to find your published image

docker build -t ps-vue-dev:0.0.1 ./Dockerfiledev

docker build -f Dockerfiledev -t ps-vue-dev:0.0.6 .

docker image tag ps-vue:0.0.7 cahillsf/ps-vue-dev:0.0.7
docker image push cahillsf/ps-vue:0.0.7

from vue container
apk --no-cache add curl
apk --no-cache add nano

curl -v http://ps-flask-service:8000/cards

PS_FLASK_SERVICE_SERVICE_HOST:PS_FLASK_SERVICE_SERVICE_PORT

front end is now connection to backend through the configuration in funvue/nginx.conf

seems like all backend routes will be prepended with /api and forwarded along

need to make sure the mongodb connection uri workss