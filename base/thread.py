import threading
from .models import *
from django.contrib.auth.models import User
from faker import Faker
import random
from .models import Product, Customer

# Faker in library to create dummy records.
fake = Faker()


class CreateUserThread(threading.Thread):
    
    def __init__(self, total):
        self.total = total
        threading.Thread.__init__(self)

    def run(self):
        try:
            print('Thread executed..')
            for i in range(self.total):
                print(i)
                first_name = fake.name()
                last_name = fake.name()
    
                User.objects.create(
                    username = "".join(first_name.split()),
                    email = f"{first_name}.{last_name}@gmail.com",
                    first_name = first_name,
                    last_name = last_name,
                    
                )

        except Exception as e:
            print(e)


class CreateCustomerThread(threading.Thread):
    
    def __init__(self, total):
        self.total = total
        threading.Thread.__init__(self)

    def run(self):
        try:
            print('Thread executed..')
            for i in range(self.total):
                print(i)

                first_name = fake.name()
                last_name = fake.name()   

                Customer.objects.create(
                    username = "".join(first_name.split()),
                    first_name = first_name,
                    last_name = last_name,
                    email = f"{first_name}.{last_name}@gmail.com",
                    latitude = fake.latitude(),
                    longitude = fake.longitude(),
                   
                )

        except Exception as e:
            print(e)

