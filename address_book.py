from faker import Faker
fake = Faker()
card_list = []
greet = 'Kontaktuj sie z'
class Card:
   def __init__(self, name, address, email, company, job, phone):
       self.name = name
       self.address = address
       self.email = email
       self.company = company
       self.job = job
       self.phone = phone

   def __repr__(self):
       return f'{self.name}, {self.address}, {self.email}, {self.company}, {self.job}, {self.phone}'

   def contact (self):
       return f' Kontaktuj się z {self.name}, adres {self.address}, email {self.email}'
   @property
   def _name_len (self):
       return f'Długosć imienia {len(self.name)}'
for i in range (0, 5):
       card_list.append(Card(name = fake.name(), address = fake.address(), email = fake.email(), company = fake.company(), job=fake.job(), phone=fake.phone_number()))
sorted(card_list, key=lambda address_book: address_book.job)
print(card_list)

