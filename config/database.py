from peewee import *

connection = PostgresqlDatabase(
    'postgres',
    port=5432,
    user='postgres',
    password='postgres'
)