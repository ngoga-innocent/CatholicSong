from rest_framework import serializers
from .models import Users


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields=['id','first_name','last_name','email','username','password','musician','profile']
        # fields='__all__'
        extra_kwargs={
            "password":{'write_only':True},
            "first_name":{"required":False},
            "last_name":{"required":False}

        }

        # def create(self,validated_data):
        #     password=validated_data.pop('password',None)
        #     instance=self.Meta.Model(**validated_data)
        #     if password is not None:
        #         instance.set_password(password)
        #     instance.save()
        #     return instance

