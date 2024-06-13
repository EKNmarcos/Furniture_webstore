from django.contrib import admin
from django.urls import path, include
from .views import AuthenticationView

app_name="authentication"

urlpatterns = [
	path('user/', AuthenticationView.as_view(), name="user_auth")
]