from django.shortcuts import render, HttpResponse
from .models import Furniture, Category
from .error.error_handler import EmptyRequestException
from .entities import Shopcart
from django.contrib.auth.forms import UserCreationForm
import json


# Create your views here.
def home(request):
      
      
      form = UserCreationForm() 
      selected_categories = ["Mesa", "Silla", "Cama", "Otros"]
      home_categories = Category.objects.all()
      furnitures = []
            
      for category in home_categories:
                  
            if category.nombre in selected_categories:
                        
                  furnitures.append(
                              
                        Furniture.objects.filter(
                                    
                                    categoria=category
                              
                        ).first()
                              
                  )
                        
      # print(furnitures)
            
      return render(request, 'home.html', {'furnitures': furnitures, 'categories': home_categories, 'form': form})


def about_us(request):
      
      return render(request, 'about.html')


def shop(request):
      
      furnitures = Furniture.objects.all()
      
      return render(request, 'brand.html', {'furnitures': furnitures})


def furniture(request, category=None):
      
      furniture = []
      categorias = Category.objects.all()
      
      if category is not None:
            
            categoria = Category.objects.filter(nombre=category)
            
            furnitures_first = Furniture.objects.filter(categoria__id__in=categoria)[:2]
            furnitures_second =  Furniture.objects.filter(categoria__id__in=categoria)[2:4]
            
            return render(request, 'trending.html', {'furnitures_first': furnitures_first,'furnitures_second':  furnitures_second, 'categories': categorias})
		
      else:
            
            
            
            for index, categoria in enumerate(categorias, start=0):
                  
                  if index < 4:
                        
                        furniture.append(
							Furniture.objects.filter(
												categoria=categoria
							).first()
				)
                        
            return render(request, 'trending.html', {'furnitures_first': furniture[:2], 'furnitures_second': furniture[2:4], 'categories': categorias})
      


def contact_us(request):
      
      if request.method == "POST":
            
            name = request.POST.get('nombre')
            email = request.POST.get('correo')
            phone = request.POST.get('telf')
            message = request.POST.get('mensaje')
                  
            print("Name -> " + name)
            print("Email -> " + email)
            print("Phone -> " + phone)
            print("Message ->" + message)
      
      return render(request, 'contact.html')

def shopcart(request):
      
      cart = Shopcart(request)
      
      return render(request, 'shopcart.html', {'shopcart': cart.shopcart})

def add_to_cart(request, id_producto):
      
      if request.method == "POST":
            
            data = json.loads(request.body)
            
            id_prod = data.get('id_producto', None)
            
            if id_prod is not None:
                  
                  try:
                        
                        shopcart = Shopcart(request)
                        furniture = Furniture.objects.get(id=id_prod)
                        shopcart.add(furniture)
                        return HttpResponse(f"Thanks for adding the product {furniture.descripcion}")
                  
                  except:
                        
                        raise Exception("An error ocurred")    
                  
            else:
                  
                  raise EmptyRequestException(
								sprocname="Views - add_to_cart()",
								err_number=98,
								err_description="The request has missing param 'id_producto'. "
			)
                  
                  
