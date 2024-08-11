class Products():

    def __init__(self,product_id, product_name, product_price):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price

    def display_product_info(self):
        print(f"{self.product_id} - {self.product_name} - ${self.product_price: .2f})")

class Book(Products):
    def __init__(self, product_id, product_name, product_price):
        super().__init__(product_id, product_name, product_price)
                
    def display_book_info(self):
        print(f"{self.product_id} - {self.product_name} - ${self.product_price: .2f} {self.author} - {self.genre}")


class Clothing(Products):
    def __init__(self, product_id, product_name, product_price):
        super().__init__(product_id, product_name, product_price)
    def display_clothing_info(self):
        print(f"{self.product_id} - {self.product_name} - ${self.product_price: .2f} {self.size} - {self.color}")


class Electronics(Products):
    def __init__(self, product_id, product_name, product_price):
        super().__init__(product_id, product_name, product_price)
    def display_electronics_info(self):
        print(f"{self.product_id} - {self.product_name} - ${self.product_price: .2f} {self.brand} - {self.style}")

  
my_new_book = Book("7844154", "Pet Semetary", 20)
my_new_book.author = "Stephen King"
my_new_book.genre = "Horror"
my_new_book.display_book_info()
my_new_coat = Clothing("9985487", "The Cold Buster 5000", 80)
my_new_coat.size = "XL"; my_new_coat.color = "Black"
my_new_coat.display_clothing_info()
my_new_cellphone = Electronics("855140", "Galaxy Thin", 850)
my_new_cellphone.brand = "Samsung"; my_new_cellphone.style = "Slim"
my_new_cellphone.display_electronics_info()












    
        