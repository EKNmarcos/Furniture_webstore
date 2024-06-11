from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
      
      list_display = ['nombre', 'descripcion', 'created_at', 'updated_at']
	
class FurnitureAdmin(admin.ModelAdmin):
      
      def img(self, obj):
            
            return format_html(f"<img src='{obj.imagen}' alt='Imagen de {obj.descripcion} width='200px'>")
      
      list_display = ['img', 'descripcion', 'valoracion', 'precio' ]

class SubscriptionAdmin(admin.ModelAdmin):
      
      def user_name(self, obj):
            
            user = User.objects.filter(username=obj.user).first()
            
            return user.username
      
      list_display = ['user_name', 'price', 'plan', 'sign_up_date']
      
      
admin.site.register(Category, CategoryAdmin)
admin.site.register(Furniture, FurnitureAdmin)
admin.site.register(Subscription, SubscriptionAdmin)