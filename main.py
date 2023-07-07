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
    shipping_option1.shipping_method = "standard"
    shipping_option1.shipping_cost = shipping_option1.get_shipping_cost()

    shipping_option2.shipping_method = "express"
    shipping_option2.shipping_cost = shipping_option2.get_shipping_cost()

    # Print the shipping options and costs
    print(f"Shipping option for {shop1.name} from {carrier1.name}:")
    print(f"Shipping method: {shipping_option1.shipping_method}")
    print(f"Shipping cost: {shipping_option1.shipping_cost}")

    print()

    print(f"Shipping option for {shop2.name} from {carrier2.name}:")
    print(f"Shipping method: {shipping_option2.shipping_method}")
    print(f"Shipping cost: {shipping_option2.shipping_cost}")


if __name__ == "__main__":
    main()