from faker import Faker
fake = Faker()


class BaseContact:
   def __init__(self, name, address, email, phone):
       self.name = name
       self.address = address
       self.email = email
       self.phone = phone
   def __repr__(self):
       return f'{self.name}, {self.address}, {self.email}, {self.phone}'
   def contact (self):
       return f' Kontaktuj się z {self.name}, adres {self.address}, email {self.email}, telefon {self.phone}'
   @property
   def label_lenght (self):
       return f'Długosć imienia {len(self.name)}'

class BuisenesContact(BaseContact):
    def __init__(self, job, company, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job = job
        self.company = company

def create_contacts():
    card_list = []
    a = int(input('podaj typ wizytówki 2 biznesowa, 1 zwykła...'))
    b = int(input('podaj ilość wygenerowanych wizytówek ...'))
    if a == 1:
        for i in range(b):
            card_list.append(BaseContact(name=fake.name(), address=fake.address(), email=fake.email(), phone=fake.phone_number()))
        sorted(card_list, key=lambda BaseContact: BaseContact.name)
    else:
        for i in range(b):
            card_list.append(BuisenesContact(name=fake.name(), address=fake.address(), email=fake.email(), phone=fake.phone_number(), job=fake.job(),
                                             company=fake.company()))
        sorted(card_list, key=lambda BuisenesContact: BuisenesContact.name)

    return print(card_list)

create_contacts()

