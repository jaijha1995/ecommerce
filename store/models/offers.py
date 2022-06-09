from itertools import product
from django.db import models
from uuid import uuid4

from psycopg2 import Timestamp

from store.models.customer import Customer
from store.models.product import Product

class offer(models.Model):
    pers = models.IntegerField(default='')
    per = models.UUIDField(default=uuid4, primary_key=True, db_index=True, editable=False)
    leave = models.ForeignKey(Product,on_delete=models.CASCADE)
    Discount = models.ForeignKey(Customer, related_name='coustomer', on_delete=models.CASCADE, default='')
    Timestamp = models.DateTimeField()



 
    class Meta:
        db_table = "offer"

    def __str__(self):
        return str(self.offer)