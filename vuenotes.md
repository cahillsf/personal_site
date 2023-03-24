## TO DO

- make sure DD instrumentation works
  * ~~passing in RUM envvars to Vue -in k8s~~
  
- containerize 
  * ~generate images for kube deployment~

### MongoDB
  * configure as statefulset - protect against data loss
  
### VUE
- ~~debounce window resize event listener~~
- style
  * fix up dropdown menu
    - if you are on page and select page from dropdown - do something (i.e. collapse the menu)
    - make menu within menu for projects
    - adjust for full size page button as well (remove any click responsne styling to make it clear to the user they are already at the selected page)
  * add breakpoint for large screens (increase grid-row gap?  maybe add some rows?)-- so bottom bar is always at bottom -- maybe there's an easier fix here....
  * full size cards for smaller screens
  * make it clearer that buttons are clickable
  * ~~copy in custom style sheet~~
  * ~~better routing--> can i create a router-link within a different element?~~
  * ~~styling-- figure out a way to keep theming (currently in nodemodules which are in the .gitignore)~~

  * ~~hide dropdown menu after user has returned to full page view so that when the browser size is reduced below the breakpoint, it will not be visible~~

  * ~~add CAPTCHA to form submission~: captcha admin: https://www.google.com/recaptcha/admin/site/512912889~~

### production build
  * updating all sensitive info for config -- MongodDB users/pws/access, flask userrole and pword -- as envvars
  * ~~writing kube yaml deployment~~
  * ~~update how services are accessed within k8s cluster - is it necessary to expose as `NodePort`?~~ NO
  * ~~working AWS K8s config~~
  * ~~https encryption - (in progress)~~
  * assess aws networking/sgs/etc
  * sourcemap upload in `docker_entrypoint_apm.sh`
  * unified service tagging
  * modsecurity - finish honeypot config
  * go live
  * ~~Merging to `adding_k8s_config` to `staging` is default-ssl-certificate needed in the `ingress-nginx-controller` command args in `nginx-elb.yaml` (https://a.cl.ly/04uExqo6)~~




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

## Secure Deployment of mongod statefulset
$ TMPFILE=$(mktemp)
$ /usr/bin/openssl rand -out $TMPFILE -base64 741
$ kubectl create secret generic shared-bootstrap-data --from-file=internal-auth-mongodb-keyfile=$TMPFILE
$ rm $TMPFILE



## Minikube

* minikube service --url ps-vue-service


Building a local image and pushing to your Docker Hub registry is very straightforward if you have an image you'd like to make public
Build the image locally: in your terminal, navigate to the directory containing your Dockerfile, then run the following command: `docker build -t <IMAGE_NAME> .`
Tag the image with the following command: `docker image tag <IMAGE_NAME> <DOCKER_USERNAME>/<IMAGE_NAME>:<TAG>`
Push the image to your Docker Hub using the following command: `docker image push <DOCKER_USERNAME>/<IMAGE_NAME>:<TAG>`
Log in to Docker Hub to find your published image

docker build -f Dockerfile-apm -t ps-vue:k8s-0.0.1 .
docker build -f Dockerfile-ss2 -t ps-mongo:ss2 .

docker image tag ps-vue:k8s-0.0.1 cahillsf/ps-vue:k8s-0.0.1

docker image tag ps-vue:apm cahillsf/ps-vue:apm
docker image push cahillsf/ps-vue:k8s-0.0.1

from vue container
apk --no-cache add curl
apk --no-cache add nano

curl -v http://ps-flask-service:8000/cards

PS_FLASK_SERVICE_SERVICE_HOST:PS_FLASK_SERVICE_SERVICE_PORT

front end is now connection to backend through the configuration in funvue/nginx.conf

seems like all backend routes will be prepended with /api and forwarded along

need to make sure the mongodb connection uri workss


look for this in style sheet 
/*cahill steve custom theme here comment*/

./docker_push.sh -t k8s -r cahillsf -i ps-vue -p ./funvue
./docker_push.sh -t k8s -r cahillsf -i ps-mongo -p ./mongo-db
./docker_push.sh -t 0.1.0 -r cahillsf -i ps-flask -p ./flask-server


curl -d "secret=<SECRET>&response=<RESPONSE_TOKEN>" -X POST https://www.google.com/recaptcha/api/siteverify


docker compose -f docker-compose-fromfile.yml up --build 


### This is the bash script to initialize the ReplicaSet once the StatefulSet has been deployed

./mongod_init_script.sh <ROOT_PASSWORD>

* should have the PV be a XFS formatted volume: https://www.mongodb.com/docs/manual/administration/production-notes/#mongodb-on-linux
  - https://devopscube.com/mount-ebs-volume-ec2-instance/

### MongoDB Operato

kubectl create namespace mongodb

kubectl create secret generic my-mongodb-user-password -n mongodb --from-literal="password=TXs3ZsuIqT-pQFvwxOec"

docker compose -f docker-compose-fromfile.yml up --build 

kubectl port-forward service/ps-vue-service 80:80

 kubectl patch svc ps-vue-service -p '{"spec":{"externalIPs":["127.0.0.1"]}}'



## Project honeypot

https://www.projecthoneypot.org/manage_honey_pots.php