from django.test import TestCase
from .models import Seller
from  rest_framework.test import APIClient 
import json

class SellerModelTests(TestCase):
    
    def test_class_str(self):
        seller=Seller()
        seller.name="Bruna"
    
        self.assertEquals(seller.__str__(),"Bruna")

    def test_to_dict(self):
        seller=Seller()
        seller.name="Bruna"
        seller.email="bruna@example.com"

        result_seller={
            "id":None,
            "name":"Bruna",
            "email":"bruna@example.com"
        }

        self.assertEquals(seller.to_dict(),result_seller)

    def test_class_str_without_name(self):
        seller=Seller()
        self.assertEqual(seller.__str__(),"")


class ProductModelTests(TestCase):

    def product_class_str(self):
        product = Product()
        product.name = "Cadeira"

        self.assertEquals(product.__str__(), "Cadeira")


    def product_to_dict(self):
        product = Product()
        product.name = "Cadeira"
        product.price = 2000
        product.seller = "Bruna"
        product.quantity = 10
        product.status = "Active"


        result_product= {
            "id": None,
            "name": "Cadeira",
            "price":2000,
            "seller":"Bruna",
            "quantity":10,
            "status": "Active"        
        
        }


        self.assertEquals(product.to_dict(), result_product)

        

    


