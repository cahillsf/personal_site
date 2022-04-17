#!/bin/bash
##
# Script to connect to the first Mongod instance running in a container of the
# Kubernetes StatefulSet, via the Mongo Shell, to initalise a MongoDB Replica
# Set and create a MongoDB admin user.
#
# IMPORTANT: Only run this once all 3 StatefulSet mongod pods are shown with
# status running (to see pod status run: $ kubectl get all)
##

# Check for password argument
if [[ $# -eq 0 ]] ; then
    echo 'You must provide one argument for the password of the "main_admin" user to be created'
    echo '  Usage:  configure_repset_auth.sh MyPa55wd123'
    echo
    exit 1
fi

# Initiate MongoDB Replica Set configuration
echo "Configuring the MongoDB Replica Set"
kubectl exec mongod-0 -c mongod-container -- mongo --eval 'rs.initiate({_id: "MainRepSet", version: 1, members: [ { _id: 0, host: "mongod-0.mongodb-service.default.svc.cluster.local:27017" } ]});'
echo

# Wait for the MongoDB Replica Set to have a primary ready
echo "Waiting for the MongoDB Replica Set to initialise..."
kubectl exec mongod-0 -c mongod-container -- mongo --eval 'while (rs.status().hasOwnProperty("myState") && rs.status().myState != 1) { print("."); sleep(1000); };'
#sleep 2 # Just a little more sleep to ensure everything is ready!
sleep 20 # More sleep to ensure everything is ready! (3.6.0 workaround for https://jira.mongodb.org/browse/SERVER-31916 )
echo "...initialisation of MongoDB Replica Set completed"
echo

# Create the admin user (this will automatically disable the localhost exception)
echo "Creating user: 'main_admin'"
kubectl exec mongod-0 -c mongod-container -- mongo --eval 'db.getSiblingDB("admin").createUser({user:"main_admin",pwd:"'"${1}"'",roles:[{role:"root",db:"admin"}]});'
echo

# # Initiate MongoDB Replica Set configuration
echo "Configuring the db initialization"
kubectl exec mongod-0 -c mongod-container -- mongosh --username main_admin --password example /usr/scripts/init2.js
echo "done initializing"

echo "Populating homepage collection"
kubectl exec mongod-0 -c mongod-container -- mongoimport -u "main_admin" -p "example" --type csv --authenticationDatabase admin -d sitecontent -c cards --headerline /usr/scripts/homepage.csv
echo "Finished populating db"

echo "populating users collection"
kubectl exec mongod-0 -c mongod-container -- mongoimport -u "main_admin" -p "example" --type csv --authenticationDatabase admin -d sitecontent -c users --headerline /usr/scripts/users.csv
echo "finished populating users collection"

