from django.test import TestCase
from .models import Seller, Product
from rest_framework.test import APIClient
import json


class SellerModelTests(TestCase):

    def test_class_str(self):
        seller = Seller()
        seller.name = "Bruna"

        self.assertEquals(seller.__str__(), "Bruna")

    def test_to_dict(self):
        seller = Seller()
        seller.name = "Bruna"
        seller.email = "bruna@example.com"

        result_seller = {
            "id": None,
            "name": "Bruna",
            "email": "bruna@example.com"
        }

        self.assertEquals(seller.to_dict(), result_seller)

    def test_class_str_without_name(self):
        seller = Seller()
        self.assertEqual(seller.__str__(), "")


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

        result_product = {
            "id": None,
            "name": "Cadeira",
            "price": 2000,
            "seller": "Bruna",
            "quantity": 10,
            "status": "Active"

        }

        self.assertEquals(product.to_dict(), result_product)


class SellerViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Seller.objects.create(name="Bruna", email="bruna@example.com")

    def test_get(self):
        client = APIClient()
        response = client.get('/produtos/sellers/')

        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)

        self.assertEqual(data.get('count'), 1)

        seller_first = data.get('results')[0]

        self.assertEqual(seller_first.get("name"), "Bruna")
        self.assertEqual(seller_first.get("email"), "bruna@example.com")

    def test_post(self):
        client = APIClient()
        response = client.post('/produtos/sellers/', {
            "name": "Bruna",
            "email": "bruna@example.com"
        })

        self.assertEqual(response.status_code, 201)
        self.assertEquals(Seller.objects.count(), 2)
        self.assertEquals(Seller.objects.last().name, "Bruna")


class ProductViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Product.objects.create(name="Cadeira", price=250, quantity=2, status="Active")

    def test_get(self):
        client = APIClient()
        response = client.get('/produtos/')

        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)
        self.assertEqual(data.get('count'), 1)

        product_first = data.get('results')[0]

        self.assertEqual(product_first.get("name"), "Cadeira")
        self.assertEqual(product_first.get("price"), 250)
        self.assertEqual(product_first.get("quantity"), 2)
        self.assertEqual(product_first.get("status"), "Active")

    def test_post(self):
        client = APIClient()
        response = client.post('/produtos/', {
            "name": "Mesa",
            "price": 300,
            "quantity": 2,
            "status": "ACTIVE"
        })

        self.assertEqual(response.status_code, 201)
        self.assertEquals(Product.objects.count(), 2)
        self.assertEquals(Product.objects.last().name, "Mesa")
