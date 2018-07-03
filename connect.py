import psycopg2

class connect:

    def __init__(self, db="northwind", user="postgres" , password  = "654321"):
        try:
            self.conn = psycopg2.connect(database=db, user=user,password = password)
            self.cur = self.conn.cursor()
        except:
            print("Error")


    def query(self, query):
        self.cur.execute(query)

    def close(self):
        self.cur.close()
        self.conn.close()
      

    #
    # conn =  psycopg2.connect("dbname='northwind' user='postgres' password='654321'")
    # cur = conn.cursor()
