from faker import Faker
fake = Faker()
name_list = []
class address_book:
   def __init__(self, name, address, email, phone):
       self.name = name
       self.address = address
       self.email = email
       self.phone = phone
