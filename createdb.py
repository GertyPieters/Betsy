from models import db, User, Product, Transaction, Tag
import os


def populate_test_database():
    cwd = os.getcwd()
    database_path = os.path.join(cwd, "betsy.db")
    if os.path.exists(database_path):
        os.remove(database_path)
        
    db.connect()

    db.create_tables([
        User,
        Product,
        Tag,
        Transaction
    ])

    users = [["Henk Henkers", "Henkstraat 40", "80NL300"], ["Johan Johanners", "Jannerstraat 37", "20NL9032"], ["Maartje Maarters", "Maartenslaan 543", "11NL8945"]]
    products = [["Pants", "Black jeans wide leg", 35, 3, 3, "Pants"], ["Sport socks", "White sport socks", 9.79, 10, 1, "Socks"], ["Vest blue", "Blue woolen vest long sleeve", 23.50, 4, 2, "Vests"], ["Vest green", "Green short vest", 27.30, 6, 2, "Vests"], ["T-shirt", "Plain white shirt short sleeve", 19.90, 10, 3, "Tshirts"]]
    tags = ["Shoes", "Pants", "Sweaters", "Hats", "Socks", "Vests", "Tshirts", "Shorts", "Coats"]
    transactions = [[3, 4, 1], [2, 2, 2], [2, 1, 2]]
            
    for user in users:
        User.create(name=user[0], address=user[1], iban=user[2])
        
    for product in products:
        Product.create(name=product[0], description=product[1], price_per_unit=product[2], quantity=product[3], owner=product[4], tags=product[5])

    for tag in tags:
        Tag.create(name=tag)

    for transaction in transactions:
        Transaction.create(buyer=transaction[0], product=transaction[1], quantity=transaction[2])
        
    db.close


if __name__ == "__main__":
    populate_test_database()