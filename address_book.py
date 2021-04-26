from faker import Faker
fake = Faker()
name_list = []
class address_book:
   def __init__(self, name, address, email, company, job):
       self.name = name
       self.address = address
       self.email = email
       self.company = company
       self.job = job
   def __repr__(self):
       return repr((self.name, self.address, self.email, self.company, self.job))
bc_one=address_book(name = fake.name(), address = fake.address(), email = fake.email(), company = fake.company(), job = fake.job())
bc_two=address_book(name = fake.name(), address = fake.address(), email = fake.email(), company = fake.company(), job = fake.job())
bc_tree=address_book(name = fake.name(), address = fake.address(), email = fake.email(), company = fake.company(), job = fake.job())
bc_four=address_book(name = fake.name(), address = fake.address(), email = fake.email(), company = fake.company(), job = fake.job())
bc_five=address_book(name = fake.name(), address = fake.address(), email = fake.email(), company = fake.company(), job = fake.job())
name_list = [bc_one, bc_two, bc_tree, bc_four, bc_five]
sorted(name_list, key=lambda address_book: address_book.job)
print(name_list)