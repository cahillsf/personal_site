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