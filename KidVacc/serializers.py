from django.db.models import fields
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Child, Parent, Hospital_Details, Hospital_Type,  Appointment
from django.contrib.auth import get_user_model
from rest_auth.registration.serializers import RegisterSerializer
<<<<<<< HEAD
=======

>>>>>>> e70e3fac976cc3bdc4c71f1d3b6437393e7635d0
# creating a model serializer

class ChildSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Child
        fields = '__all__'


class ParentSerializer(serializers.ModelSerializer):

    
    First_name = serializers.CharField(required=True,
                                    validators=[UniqueValidator(queryset=Parent.objects.all())])

    Last_name = serializers.CharField(required=True,
                                    validators=[UniqueValidator(queryset=Parent.objects.all())])

    Gender = serializers.CharField(required=True,
                                    validators=[UniqueValidator(queryset=Parent.objects.all())])

    Email_address = serializers.EmailField(required=True,)

    Password = serializers.CharField(min_length=8, write_only=True)

    Phone_number = serializers.IntegerField(required=True,
                                    validators=[UniqueValidator(queryset=Parent.objects.all())])

    images = serializers.ImageField(required=False)


    # def create(self, validated_data):
    #     parent = Parent.objects.create(validated_data['First_name'],
    #                                     validated_data['Last_name'],
    #                                     validated_data['Gender'],
    #                                     validated_data['Email_address'],
    #                                     validated_data['Password'],
    #                                     validated_data['Phone_number'],
    #                                     validated_data['images']
    #                                         )
                                           
    #     return parent
    class Meta:
        model = Parent
        fields = '__all__'

class NormalParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        exclude = ('user',)
    
class UserParentUpdateSerializer(serializers.ModelSerializer):
    parent = ParentSerializer()
    class Meta:
        model = get_user_model() 
        fields = '__all__'      
    
    def update(self,instance,validated_data):
        instance.username = validated_data.get('username',instance.username)
        instance.email = validated_data.get('email',instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        parent_data = validated_data.pop('parent')
        # first_name = validated_data.pop('first_name')
        # last_name = validated_data.pop('last_name')
        # email = validated_data.pop('email')
        user  = get_user_model().objects.get(username = instance.username)
        # user_data = {"first_name":f"{first_name}","last_name":"last_name","email":f"{email}"}
        # user_serializer = UserSerializer(data= user_data)
        parent = Parent.objects.get(user=user)
        parent_serializer = ParentSerializer(data=parent_data)
        
        if parent_serializer.is_valid():
            parent_serializer.update(parent,parent_data)
        instance.save()
        return instance

class Hospital_DetailsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Hospital_Details
        fields = '__all__'


class Hospital_TypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Hospital_Type
        fields = '__all__'



class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
<<<<<<< HEAD
        fields = '__all__'

# class MultipleChoiceFieldSerializer(fields.MultipleChoiceField):
=======
        fields = '__all__'
>>>>>>> e70e3fac976cc3bdc4c71f1d3b6437393e7635d0
