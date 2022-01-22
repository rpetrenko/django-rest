from decimal import Decimal
from django.test import TestCase
from main import models


class TestModel(TestCase):
    def test_active_manager_works(self):
        models.Product.objects.create(
            name="active 1", price=Decimal("10.00")
        )
        models.Product.objects.create(
            name="active 2", price=Decimal("10.00")
        )
        models.Product.objects.create(
            name="not active", price=Decimal("10.00"), active=False
        )
        self.assertAlmostEqual(len(models.Product.objects.active()), 2)