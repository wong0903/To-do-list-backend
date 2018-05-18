import psycopg2

def connect1():
	conn = psycopg2.connect("dbname='Test' host='localhost' user='postgres' password='poliknight1'")
	return conn
