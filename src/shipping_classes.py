class Carrier:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def connect_to_shop(self, shop):
        return ShippingOption(self.name, self.country, shop)


class ShippingOption(Carrier):
    def __init__(self, name, country, shop):
        super().__init__(name, country)
        self.shop = shop
        self.shipping_method = ""
        self.shipping_cost = 0.0

    def get_shipping_cost(self):
        if self.shipping_method == "standard":
            cost_per_kg = 0.5
        elif self.shipping_method == "express":
            cost_per_kg = 1.0
        else:
            cost_per_kg = 0.75

        return self.shop.package_weight * cost_per_kg


class Shop:
    def __init__(self, name, package_weight):
        self.name = name
        self.package_weight = package_weight