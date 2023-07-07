from src.shipping_classes import Shop, Carrier


def main():
    # Create shop instances
    shop1 = Shop("Shop 1", 2.5)
    shop2 = Shop("Shop 2", 1.8)

    # Create carrier instances
    carrier1 = Carrier("Carrier 1", "Country 1")
    carrier2 = Carrier("Carrier 2", "Country 2")

    # Connect carriers to shops
    shipping_option1 = carrier1.connect_to_shop(shop1)
    shipping_option2 = carrier2.connect_to_shop(shop2)

    # Set shipping method and cost
    shipping_option1.set_shipping_method("standard")
    shipping_option1.set_package_weight(2.5)

    shipping_option2.set_shipping_method("express")
    shipping_option2.set_package_weight(1.8)

    shipping_cost1 = shipping_option1.get_shipping_cost()
    shipping_cost2 = shipping_option2.get_shipping_cost()

    # Print the shipping options and costs
    print(f"Shipping option for {shop1.name} from {carrier1.name}: {shipping_cost1}")

    print()

    print(f"Shipping option for {shop2.name} from {carrier2.name}: {shipping_cost2}")

if __name__ == "__main__":
    main()