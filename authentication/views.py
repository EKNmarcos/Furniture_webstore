from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages


# Create your views here.
class AuthenticationView(View):
      
      def get(self, request):
            
            form = UserCreationForm
            
            return render(request, 'home.html', {'form': form})
      
      def post(self, request): #this handles the POST request
            
            form = UserCreationForm(request.POST) # receive the form data
            
            if form.is_valid(): # check if is valid
                  
                  usuario = form.save() # create the user
                  
                  login(request, usuario) # login
                  
                  return redirect('home') # redirect
   
            else:
                  
                  for message in form.error_messages:
                        
                        messages.error(request, form.error_messages[message])
                        
                  return render(request, 'home.html', {'form': form})
                  