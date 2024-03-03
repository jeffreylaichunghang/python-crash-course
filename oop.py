class User:
    def log(self):
        print(self)

class Teacher(User):
    def log(self):
        # override the user log method
        print('I am a teacher')

class Customer(User):
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type
        print("customer created ")

    @property # function to get property
    def name(self):
        print('getting name')
        return self._name

    @name.setter
    def name(self, name):
        print('setting name')
        self._name = name

    def update_membership(self, new_membership):
        self.membership_type = new_membership

    def read_customer(self):
        print("Read customer from DB")

    def __str__(self) -> str:
        print("converting to string")
        return self.name + " " + self.membership_type

    def print_all_customers(customers):
        for customer in customers:
            print(customer)

    def __eq__(self, other):
        if self.name == other.name and self.membership_type == other.membership_type:
            return True

        return False

    # overriding method
    __hash__ = None
    __repr__ = __str__ # print in readable format


customers = [Customer('Jeff', 'Gold'), Customer('Cherry', 'Silver'), Teacher()]
# print(customers[0].membership_type)
# customers[0].update_membership('Silver')
# print(customers[0].membership_type)
# print(customers[0])
# Customer.print_all_customers(customers)
# print(id(customers[0]), id(customers[1]))
# print(customers)
# print(customers[0].name)
# customers[0].log()
for customer in customers:
    customer.log()
