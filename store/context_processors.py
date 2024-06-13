from django.contrib.auth.forms import UserCreationForm

def get_login_form(request):
      
      form = UserCreationForm()
      
      return {
		'form': form
	}