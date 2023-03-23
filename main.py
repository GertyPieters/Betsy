from peewee import fn
from models import User, Product, Transaction
from createdb import User, Product, Transaction
import enchant

__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"


def search(term):
    dict = enchant.Dict("en_US")
    if dict.check(term) == False:
        suggestions = dict.suggest(term)
        if suggestions:
            term = suggestions[0]
    query = (Product
             .select()
             .where(fn.lower(Product.name.contains(fn.lower(term)) | Product.description.contains((fn.lower(term))))))
    products = set()
    for product in query:
        products.add(product.name)
    print(products)

#search("sovks")

def list_user_products(user_id): 
    product_set = set()
    products = (Product
                .select(Product, User)
                .join(User)
                .where(Product.owner==user_id))
    for item in products:
        product_set.add(item.name)
    print(list(product_set))

#list_user_products(2)

def list_products_per_tag(tag_id):
    tag_products = set()
    products = Product.select().where(Product.tags == tag_id)
    for product in products:
        tag_products.add(product.name)
    print(list(tag_products))
    
#list_products_per_tag("Socks")



def update_stock(product_id, new_quantity):
    product = Product.get(Product.id == product_id)
    product.quantity = new_quantity
    print(product.name, product.quantity)


def purchase_product(product_id, buyer_id, quantity):
    product = Product.get(Product.id == product_id)
    if product.quantity >= quantity:
        product.quantity -= quantity
        product.save
    transaction = Transaction(buyer_id=buyer_id, product_id=product_id, quantity=quantity)
    transaction.save


def remove_product(product_id):
    product = Product.get(Product.id == product_id)
    product.user.delete_instance()
    

