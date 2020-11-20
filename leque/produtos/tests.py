from django.test import TestCase
from .models import Seller

class SellerModelTests(TestCase):
    
    def test_class_str(self):
        seller=Seller()
        seller.name="Bruna"
    
        self.assertEquals(seller.__str__(),"Bruna")

    def test_to_dict(self):
        seller=Seller()
        seller.name="Bruna"
        seller.email="bruna@example.com"

        result={
            "id":None,
            "name":"Bruna",
            "email":"bruna@example.com"
        }

        self.assertEquals(seller.to_dict(),result)

    def test_class_str_without_name(self):
        seller=Seller()
        self.assertEqual(seller.__str__(),"")