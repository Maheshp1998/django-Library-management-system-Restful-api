from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

        extra_kwargs = {
            'password': {
                'write_only' : True
            }
        }

    def create(self,validated_data):
        print(validated_data)
       
        user = User.objects.create(
            username =  validated_data['username'],
            first_name =  validated_data['first_name'],
            last_name =  validated_data['last_name'],
            email =  validated_data['email'],            
        )
        if validated_data.get('password'):
           user.set_password(validated_data['password'])
           user.save()
           return validated_data

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return validated_data


class Category_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Book_Category
        fields = "__all__"
        # depth = 1      


class Book_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        depth = 1


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model =  User
        fields = ['id','first_name','last_name','email','username','password']
        extra_kwargs = {
            'password' : {
                'write_only' : True
            }
        }

    def create(self,validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save() 
        return user 
