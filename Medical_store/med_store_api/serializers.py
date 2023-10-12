from med_site.models import Medicine
from rest_framework import serializers
from django.contrib.auth import get_user_model


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = ('id', 'med_name', 'unit','dosage','stock')

class MedicineSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = ('id', 'med_name','stock')


User = get_user_model()
class UserRegister(serializers.ModelSerializer):
    password02 = serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model = User
        fields = ["username","password","email","password02"]
    def save(self):
        reg=User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
        )
        password=self.validated_data['password']
        password02=self.validated_data['password02']
        if password != password02:
            raise serializers.ValidationError({'password':'password does not match'})
        reg.set_password(password)
        reg.save()
        return reg
    
class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')

class MedicineDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = ('med_name','purpose','unit','dosage','stock')



class MedicineRegister(serializers.ModelSerializer):

    class Meta:
        model = Medicine
        fields = ('med_name','purpose','unit','dosage','stock')
    def save(self):
        med=Medicine(
            med_name=self.validated_data['med_name'],
            purpose=self.validated_data['purpose'],
            unit=self.validated_data['unit'],
            dosage=self.validated_data['dosage'],
            stock=self.validated_data['stock'],
        )
        med.save()
        return med

