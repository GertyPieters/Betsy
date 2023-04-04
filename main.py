from peewee import fn
from models import User, Product, ProductTag, Transaction
from createdb import User, Product, ProductTag, Transaction
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


def list_user_products(user_id): 
    product_set = set()
    products = (Product
                .select(Product, User)
                .join(User)
                .where(Product.owner==user_id))
    for product in products:
        product_set.add(product.name)
    print(list(product_set))


def list_products_per_tag(tag_id):
    tag_products = set()
    products = (Product
                .select(Product, ProductTag)
                .join(ProductTag)
                .where(ProductTag.tag_id == tag_id))
    for product in products:
        tag_products.add(product.name)
    print(list(tag_products))


def update_stock(product_id, new_quantity):
    product = Product.get(Product.id == product_id)
    product.quantity = new_quantity
    product.save()
    print(product.name, product.quantity)


def purchase_product(product_id, buyer_id, quantity):
    product = Product.get(Product.id == product_id)
    if product.quantity >= quantity:
        product.quantity -= quantity
        product.save()
    transaction = Transaction(buyer_id=buyer_id, product_id=product_id, quantity=quantity)
    transaction.save()


def remove_product(product_id):
    product = Product.get(Product.id == product_id)
    products = (Product
               .select(Product)
               .join(User)
               .where((Product.id == product_id) & (User.id == Product.owner)))
    for product in products:
        product.delete_instance()
        product.save()
    

def main():
    # search("sovks")
    # list_user_products(2)
    # list_products_per_tag(6)
    # update_stock(1, 5)
    # purchase_product(1, 1, 2)
    remove_product(1)


if __name__ == "__main__":
    main()



