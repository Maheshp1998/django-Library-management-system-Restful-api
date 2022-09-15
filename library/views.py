from rest_framework import viewsets
from django.shortcuts import render
from .models import Book,Book_Category
from .serializer import Book_Serializer, Category_Serializer, SignupSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
# from rest_framework.authentication import TokenAuthentication

def Indexpage(request):
    return render(request,'index.html')

class CategoryView(viewsets.ModelViewSet):
    serializer_class = Category_Serializer
    queryset = Book_Category.objects.all()


class BookView(viewsets.ModelViewSet):
    serializer_class = Book_Serializer
    queryset = Book.objects.all()


class SignupView(viewsets.ModelViewSet):
    
    serializer_class = SignupSerializer
    queryset = User.objects.filter(is_superuser=False, is_staff=False)
    

class LoginView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class StudentsView(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = Book_Serializer
    queryset = Book.objects.all()