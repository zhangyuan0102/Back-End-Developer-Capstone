from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return f'{self.name} : {str(self.price)}'

class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    reservation_date = models.DateTimeField()
    guest_count = models.IntegerField()
    special_requests = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Booking for {self.customer_name} on {self.reservation_date}"

