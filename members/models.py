from django.db import models
from django.contrib.auth.models import User



class Trainer(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='trainers/')


class Membership(models.Model):
    PLAN_CHOICES = [
        ('Standard', 'Standard'),
        ('Premium', 'Premium'),
        ('VIP', 'VIP'),
    ]
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    plan = models.CharField(max_length=20, choices=PLAN_CHOICES)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class ClassSchedule(models.Model):
    title = models.CharField(max_length=100)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)


class Payment(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_id = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)  # ✅ Razorpay webhook se TRUE karo

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.payment_id} - {'Paid' if self.paid else 'Pending'}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_premium = models.BooleanField(default=False)
