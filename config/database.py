from peewee import *

connection = PostgresqlDatabase(
    'postgres',
    host='localhost',
    port=5432,
    user='postgres',
    password='postgres'
)