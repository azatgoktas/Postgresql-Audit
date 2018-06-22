import psycopg2

conn =  psycopg2.connect("dbname='northwind' user='postgres' password='654321'")
cur = conn.cursor()
