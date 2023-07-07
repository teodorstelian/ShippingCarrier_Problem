class Carrier:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def connect_to_shop(self, shop):
        return ShippingOption(self, shop)


class ShippingOption(Carrier):
    COST_STANDARD = 0.5
    COST_EXPRESS = 1.0
    COST_DEFAULT = 0.75

    def __init__(self, carrier, shop):
        super().__init__(carrier.name, carrier.country)
        self.shop = shop
        self.shipping_method = ""
        self.shipping_cost = 0.0

    def set_shipping_method(self, method):
        valid_methods = ["standard", "express"]
        if method in valid_methods:
            self.shipping_method = method
        else:
            raise ValueError("Invalid shipping method provided.")

    def set_package_weight(self, weight):
        if weight > 0:
            self.shop.package_weight = weight
        else:
            raise ValueError("Invalid package weight provided.")

    def get_shipping_cost(self):
        if self.shipping_method == "standard":
            cost_per_kg = ShippingOption.COST_STANDARD
        elif self.shipping_method == "express":
            cost_per_kg = ShippingOption.COST_EXPRESS
        else:
            cost_per_kg = ShippingOption.COST_DEFAULT

        return self.shop.package_weight * cost_per_kg


class Shop:
    def __init__(self, name, package_weight):
        self.name = name
        self.package_weight = package_weight