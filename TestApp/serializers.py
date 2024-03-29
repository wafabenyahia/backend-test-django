from rest_framework import serializers
from TestApp.models import User, Entreprise, Responsable, Pdl


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('nom', 'prenom', 'email', 'password')

class GETUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
class EntrepriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entreprise
        fields = ('siret','raison','adressPostal','user')
class GETEntrepriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entreprise
        fields = '__all__'
class ResponsableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsable
        fields = ('nom', 'prenom', 'email', 'numTel', 'entreprise', 'status')
class GETResponsableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsable
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
class PDLSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pdl
        fields = ('pdl','type','entreprise')
class GETPDLSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pdl
        fields = '__all__'
