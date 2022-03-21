class Config(object):
    """Base config, uses staging database server."""
    TESTING = False
    DB_SERVER = 'localhost'

    @property
    def DATABASE_URI(self):  # Note: all caps
        return f"mongodb://flask-role:toor@{self.DB_SERVER}:27017/sitecontent?authSource=sitecontent"

class localConfig(Config):
    DB_SERVER = 'localhost'

class dockerConfig(Config):
    DB_SERVER = 'mongodb'

class kubernetesConfig(Config):
    DB_SERVER = 'ps-mongo-service'

class headlessConfig(Config):
    DB_SERVER = 'mongodb-service'