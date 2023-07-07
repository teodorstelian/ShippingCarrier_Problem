Create two classes, Carrier and ShippingOption, where ShippingOption is a subclass of Carrier.
Carrier should have the following attributes and methods:
 
-	name: A string representing the name of the carrier
-	country: A string representing the country of the carrier
-	connect_to_shop(): A method that takes a Shop object as an argument and returns a ShippingOption object that represents the shipping option for that shop
 
ShippingOption should inherit all of the attributes and methods of Carrier, and should also have the following additional attributes and methods:

- shipping_method: A string representing the shipping method (e.g. "express", "standard", etc).

- shipping_cost: A float representing the cost of shipping

- get_shipping_cost(): A method that calculates and returns the cost of shipping based on the weight of the package and the shipping method selected. 
If shipping_method = "standard", cost_per_kg will be 0.5, else if shipping_method = "express", cost_per_kg will be 1.0, else 0.75. The cost is calculated based on the formula: weight * cost_per_kg
 
Create a Shop class that has the following attributes:
- name: A string representing the name of the shop
- package_weight: A float representing the weight of the package
 
In addition to the above classes, create two instances of the ShippingOption class, each representing a different shipping option for a shop. 
Each instance should have its own unique set of attributes, including the weight of the package.
Finally, write code to test the functionality of both classes, making sure to test all of the methods and attributes. 
For example, you might create a loop that iterates through a list of shops, calling the connect_to_shop() method on each carrier to get the available shipping options for that shop, and then calling the get_shipping_cost() method on each shipping option to calculate the cost of shipping.

