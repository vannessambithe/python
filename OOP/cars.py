class cars():
    def __init__(self, color, deliverylocation, customer):
        self.color = color
        self.deliverylocation = deliverylocation
        self.customer = customer

customer_one = cars("pink", "Kitengela", "Vannessa")
print(customer_one.color)
print(customer_one.deliverylocation)
print(customer_one.customer)

customer_two = cars("red", "Kajiado", "Mutavi")
print(customer_two.color)
print(customer_two.deliverylocation)
print(customer_two.customer)
