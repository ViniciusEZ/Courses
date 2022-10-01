class Client:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.addresses = []

    def insert_address(self, city, state):
        self.addresses.append(Address(city, state))

    def show_addresses(self):
        for address in self.addresses:
            print(address.city, address.state)


class Address:
    def __init__(self, city, state):
        self.city = city
        self.state = state
