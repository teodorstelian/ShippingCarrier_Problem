import unittest

from src.shipping_classes import Shop, Carrier


class TestShippingClasses(unittest.TestCase):
    def test_get_shipping_cost_standard(self):
        shop = Shop("Shop 1", 2.5)
        carrier = Carrier("Carrier 1", "Country 1")
        shipping_option = carrier.connect_to_shop(shop)
        shipping_option.shipping_method = "standard"
        shipping_cost = shipping_option.get_shipping_cost()
        expected_cost = 1.25
        assert shipping_cost == expected_cost

    def test_get_shipping_cost_express(self):
        shop = Shop("Shop 2", 1.8)
        carrier = Carrier("Carrier 2", "Country 2")
        shipping_option = carrier.connect_to_shop(shop)
        shipping_option.shipping_method = "express"
        shipping_cost = shipping_option.get_shipping_cost()
        expected_cost = 1.8
        assert shipping_cost == expected_cost

    def test_connect_to_shop(self):
        shop = Shop("Shop 3", 1.2)
        carrier = Carrier("Carrier 3", "Country 3")
        shipping_option = carrier.connect_to_shop(shop)
        assert shop == shipping_option.shop
        assert carrier.name == shipping_option.name
        assert carrier.country == shipping_option.country

    def test_shipping_option_attributes(self):
        shop = Shop("Shop 4", 2.0)
        carrier = Carrier("Carrier 4", "Country 4")
        shipping_option = carrier.connect_to_shop(shop)
        shipping_option.shipping_method = "standard"
        shipping_option.shipping_cost = 1.0
        assert shipping_option.shop == shop
        assert shipping_option.name == carrier.name
        assert shipping_option.country == carrier.country
        assert shipping_option.shipping_method == "standard"
        assert shipping_option.shipping_cost == 1.0

    def test_shop_attributes(self):
        shop = Shop("Shop 5", 1.5)
        assert shop.name == "Shop 5"
        assert shop.package_weight == 1.5

    def test_set_shipping_method_invalid(self):
        shop = Shop("Shop 1", 2.5)
        carrier = Carrier("Carrier 1", "Country 1")
        shipping_option = carrier.connect_to_shop(shop)
        with self.assertRaises(ValueError):
            shipping_option.set_shipping_method("invalid_method")

    def test_set_package_weight_invalid(self):
        shop = Shop("Shop 1", 2.5)
        carrier = Carrier("Carrier 1", "Country 1")
        shipping_option = carrier.connect_to_shop(shop)
        with self.assertRaises(ValueError):
            shipping_option.set_package_weight(-1.0)


if __name__ == "__main__":
    unittest.main()