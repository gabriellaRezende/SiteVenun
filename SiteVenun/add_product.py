from app import db
from models import Product
from app import app

# Criando produtos
produtos = [
    Product(nome="Checked Short Dress", preco=12.49, imagem_one="images/shop/dress/1.jpg", imagem_two="images/shop/dress/1-1.jpg"),
    Product(nome="Slim Fit Chinos", preco=39.99, imagem_one="images/shop/pants/1.jpg", imagem_two="images/shop/pants/1-1.jpg"),
    Product(nome="Dark Brown Boots", preco=49, imagem_one="images/shop/shoes/1.jpg", imagem_two="images/shop/shoes/1-1.jpg"),
    Product(nome="Light Blue Denim Dress", preco=19.95, imagem_one="images/shop/dress/2.jpg", imagem_two="images/shop/dress/2-2.jpg"),
    Product(nome="Unisex Sunglasses", preco=11.99, imagem_one="images/shop/sunglasses/1.jpg", imagem_two="images/shop/sunglasses/1-1.jpg"),
    Product(nome="Blue Round-Neck Tshirt", preco=9.99, imagem_one="images/shop/tshirts/1.jpg", imagem_two="images/shop/tshirts/1-1.jpg"),
    Product(nome="Silver Chrome Watch", preco=129.99, imagem_one="images/shop/watches/1.jpg", imagem_two="images/shop/watches/1-1.jpg"),
    Product(nome="Men Grey Casual Shoes", preco=39.49, imagem_one="images/shop/shoes/2.jpg", imagem_two="images/shop/shoes/2-1.jpg"),
    Product(nome="Pink Printed Dress", preco=39.499, imagem_one="images/shop/dress/3.jpg", imagem_two="images/shop/dress/3-1.jpg"),
    Product(nome="Green Trousers", preco=21.99, imagem_one="images/shop/pants/5.jpg", imagem_two="images/shop/pants/5-1.jpg"),

]

# Adicionando ao banco
with app.app_context():
    with db.session.begin():
        db.session.add_all(produtos)
        db.session.commit()
print("Produtos adicionados com sucesso!")
