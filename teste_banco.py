import psycopg2 as db

class Config:
    def __init__(self):
        self.config = {
        "postgres":{
            "user": "postgres",
            "password": "123",
            "host": "127.0.0.1",
            "port": "5432",
            "database": "pydb"}
        }

"""class Connection(Config):
    def __init__(self):
        Config.__init__(self)"""

class Connection(Config):
    def __init__(self):
        #super().__init__()
        Config.__init__(self)
        try:
            self.conn = db.connect(**self.config["postgres"])
            self.cur = self.conn.cursor()
        except Exception as e:
            print("ERRO", e)
        
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.connetion.close()

    @property
    def connetion(self):
        return self.conn

    @property
    def cursor(self):
        return self.cur

    def commit(self):
        self.connetion.commit()

    def fetchall(self):
        return self.cursor.fetchall()
    
    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def querry(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()

class Person(Connection):
    def __init__(self):
        #super().__init__()
        Connection.__init__(self)

    def insert(self, *args):
        try:
            sql = "INSERT INTO person (name) VALUES (%s)"
            self.execute(sql, args)
            self.commit()
        except Exception as e:
            print("ERRO", e)


if __name__ == "__main__":
    person = Person()
    person.insert("Maria")