from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User


SUBSCRIPTION_PLAN = {
	"FREE": 'Free',
	"PERSONAL": 'Personal',
	"PROFESSIONAL": 'Professional',
	"TEAM": 'Team',
	"ENTERPRISE": 'Enterprise'
}


# Create your models here.
class Category(models.Model):
      
      id = models.UUIDField(primary_key=True, default=uuid4)
      nombre = models.CharField(default="", help_text="(silla, mesa...)")
      descripcion = models.CharField(default="", null=True, blank=True)
      created_at = models.DateField(auto_now_add=True)
      updated_at = models.DateField(auto_now_add=True)

class Furniture(models.Model):
      
      id = models.UUIDField(primary_key=True, default=uuid4)
      imagen = models.ImageField(upload_to='media/', default="assets/Logo.png")
      descripcion = models.CharField(null=False, blank=False)
      valoracion = models.CharField(default="5.0 de 5")
      precio = models.DecimalField(default=0, decimal_places=2, max_digits=8)
      categoria = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
      entrega = models.CharField(default="")
      created_at = models.DateField(auto_now_add=True)
      updated_at = models.DateField(auto_now_add=True)
      
class Subscription(models.Model):
      
      user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
      price = models.DecimalField(default=25, decimal_places=2, max_digits=8)
      plan = models.CharField(default=SUBSCRIPTION_PLAN["FREE"])
      sign_up_date = models.DateField(auto_now_add=True)
      
      