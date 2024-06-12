from .models import Furniture
from .error.error_handler import ObjectNotFoundException
import urllib.parse

class Shopcart:
      
      def __init__(self, request):
            
            """
			request: HttpRequest
      	"""
            self.request = request
            self.session = request.session
            self.shopcart = self.session.get('shopcart', {})
            
            if not self.shopcart:
                  self.session["shopcart"] = self.shopcart
            
            
            
      def save(self):
            
            self.session["shopcart"] = self.shopcart
            self.session.modified = True
            
      def add(self, furniture: Furniture):
            
            if str(furniture.id) not in self.shopcart.keys(): # if the product doesn't exist inside the shopcart
                  
                  self.shopcart[str(furniture.id)] = {
									"id": str(furniture.id),
									"image": urllib.parse.unquote(furniture.imagen.url[1:]),
         								"description": furniture.descripcion,
                 							"assessment": furniture.valoracion,
                        					"price": str(furniture.precio),
									"categoria": furniture.categoria.nombre,
									"entrega": furniture.entrega,
									"amount": 1,
			}
            else: # if the product already exists
                  
                  self.shopcart[str(furniture.id)]['amount'] += 1
                  
            self.save()
            
      def remove(self, furniture: Furniture):
            
            if str(furniture.id) not in self.shopcart.keys():
                  
                 raise ObjectNotFoundException(
                       					sprocname='Shopcart - remove()', 
                            				err_number=0, 
                            				err_description=f"Object not found in session {self.__class__.__name__}"
                            			    )
            else:
                  
                  del self.shopcart[str(furniture.id)]
                  
                  self.save()
            
      
      def subtract(self, furniture: Furniture):
            
            if str(furniture.id) not in self.shopcart.keys():
                  
                 raise ObjectNotFoundException(
                       					sprocname='Shopcart - remove()', 
                            				err_number=0, 
                            				err_description=f"Object not found in session {self.__class__.__name__}"
                            			    )
            else:
                  
                  self.shopcart[str(furniture.id)]['amount'] -= 1
                  
                  if self.shopcart[str(furniture.id)]['amount'] < 1:
                        
                        self.remove(furniture)
                        
                  self.save()
      
      def reset(self):
            
            self.shopcart = {}
            self.save()
            
            
            
            