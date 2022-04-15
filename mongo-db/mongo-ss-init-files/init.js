db = new Mongo().getDB("sitecontent");
db.createUser({
  user: 'flask-role',
  pwd: 'toor',
  roles: [
    {
      role: 'readWrite',
      db: 'sitecontent',
    },
  ],
});
db.createCollection('messages');
db.createCollection('cards');
rs.initiate({ _id: "MainRepSet", version: 1, 
members: [ 
 { _id: 0, host: "mongod-0.mongodb-service.default.svc.cluster.local:27017" } ]});
rs.status();