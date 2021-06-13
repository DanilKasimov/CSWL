from peewee import *

db = MySQLDatabase(database='cswl3orm', user='root', password='Danilka210300', host='localhost')


class BaseModel(Model):
    Id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'Id'




