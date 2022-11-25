from rest_framework import serializers
from almacen.models import Producto
from usuarios.models import User

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password')
        extra_kwargs = {
            'password':{
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            }
        }
    # Metodos para guardar el usuario:
    def create(self, validated_data):
        """ Creamos y Retornamos un usuario """
        user = User.objects.create_user(
            email = validated_data['email'], 
            username = validated_data['username'],
            password = validated_data['password']
        )
        return user
    
    # Garantizamos que el password se guarde encriptado:
    def update(self, instance, validated_data):
        """ Aplica método HASH al campo password """
        # Valido que el campo password pase la validación de validated_data:
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        # retornamos lo que hemos hecho:
        return super().update(instance, validated_data)


