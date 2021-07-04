import psycopg2 as db
import csv
import json_manager as x


class Config():
    def __init__(self):

        self.config = {
        "postgres":{
            "user": "postgres",
            "password": "123",
            "host": "127.0.0.1",
            "port": "5432",
            "database": "pydb"}
        }
        #self.config = conteudo
"""class Connection(Config):
    def __init__(self):
        Config.__init__(self)"""
        #super().__init__()
        #Config.__init__(self)
        
class Connection():
    def __init__(self):
        self.arquivo_procurado = "a.json"
        self.arquivo = x.jsonManager()
        self.conteudo = self.arquivo.read(self.arquivo_procurado)

        if self.conteudo == False:
            print(f"O arquivo {self.arquivo_procurado} não existe.")
            exit()
        else:
            self.config = self.conteudo

        try:
            self.conn = db.connect(**self.config)
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
        super().__init__()
        #Connection.__init__(self)

    def insert(self, *args):
        try:
            sql = "INSERT INTO person (name) VALUES (%s)"
            self.execute(sql, args)
            self.commit()
        except Exception as e:
            print("ERRO", e)

    def insert_csv(self, filename):
        try:
            data = csv.DictReader(open(filename, encoding = "UTF-8"))
            for row in data:
                self.insert(row["name"])
        except Exception as e:
            print("ERRO", e)

    def delete(self, id):
        try:
            sql_s = f"SELECT * FROM person WHERE id = {id}"
            if not self.querry(sql_s):
                return False
            else:
                sql_s = f"DELETE FROM person WHERE id = {id}"
                self.execute(sql_s)
                self.commit()
                return True

        except Exception as e:
            print("ERRO", e)

    def atualizar(self, id, *args):
        try:
            sql_command = f"UPDATE person SET name = %s WHERE id = {id}"
            self.execute(sql_command, args)
            self.commit()
        except Exception as e:
            print("ERRO", e)

    def search(self, *args, type_s = "name"):
        sql = f"SELECT * FROM person WHERE name LIKE %s"
        if type_s == "id":
            sql = f"SELECT * FROM person WHERE id = %s"
        data = self.querry(sql, args)
        if data:
            return data
        else:
            return "Not found"

if __name__ == "__main__":
    person = Person()
    #print(person.querry("SELECT * FROM person")) ___imprime uma tabela do BD
    #person.insert("Rafael")
    #person.insert_csv("caminho.csv")
    #person.delete(6)
    #person.atualizar(1, "alterado")
    #print(person.search(1, type_s="id")
    #print(person.search("teste")
    #x = f"%{texto_procurado}"
    #print(person.search("%teste")
    

    print("terminou")