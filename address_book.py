from faker import Faker
fake = Faker()
name_list = []
class address_book:
   def __init__(self, name, address, email, company, poz):
       self.name = name
       self.address = address
       self.email = email
       self.company = company
       self.poz = poz