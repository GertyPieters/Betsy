import peewee

db = peewee.SqliteDatabase("betsy.db")

class User(peewee.Model):
    name = peewee.CharField()
    address = peewee.CharField()
    iban = peewee.CharField()

    class Meta:
        database = db

class Tag(peewee.Model):
    name = peewee.CharField(unique=True)

    class Meta:
        database = db

class Product(peewee.Model):
    name = peewee.CharField()
    description = peewee.TextField ()
    price_per_unit = peewee.DecimalField(decimal_places=2)
    quantity = peewee.IntegerField()
    owner = peewee.ForeignKeyField(User, backref='products')
    tags = peewee.ForeignKeyField(Tag, backref='products')

    class Meta:
        database = db
 

class Transaction(peewee.Model):
    buyer = peewee.ForeignKeyField(User, backref='transactions')
    product = peewee.ForeignKeyField(Product, backref='transactions')
    quantity = peewee.IntegerField()


    class Meta:
        database = db   



    