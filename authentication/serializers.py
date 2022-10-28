from .models import User 
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from userprofile.models import TenderProfile, InputProfile, InvestorProfile, FarmerProfile





# class UserCreationSerializer(serializers.ModelSerializer):
#     username=serializers.CharField(max_length=25)
#     email=serializers.EmailField(max_length=80)
#     phone_number=PhoneNumberField(allow_null=False, allow_blank=False)

#     class Meta:
#         model=User
#         fields=['username', 'email', 'phone_number', 'password']


#     def validate(self, attrs):
#         username_exists=User.objects.filter(username=attrs['username']).exists()

#         if username_exists:
#             raise serializers.ValidationError(detail="User with username exists")
        
#         email_exists=User.objects.filter(username=attrs['email']).exists()

#         if email_exists:
#             raise serializers.ValidationError(detail="User with email exists")
        
#         phone_number_exists=User.objects.filter(username=attrs['phone_number']).exists()

#         if phone_number_exists:
#             raise serializers.ValidationError(detail="User with phonenumber  exists")


#         return super().validate(attrs)


class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmerProfile
        fields =('first_name', 'last_name')

class TenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenderProfile
        fields =('first_name', 'last_name')

class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorProfile
        fields =('first_name', 'last_name')

class InputSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputProfile
        fields =('first_name', 'last_name')




class FarmerUserCreationSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=25)
    email=serializers.EmailField(max_length=80)
    phone_number=PhoneNumberField(allow_null=False, allow_blank=False)

    profile = FarmerSerializer(required=False)

    class Meta:
        model = User
        fields = ('username','email', 'phone_number','password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        username_exists=User.objects.filter(username=attrs['username']).exists()

        if username_exists:
            raise serializers.ValidationError(detail="User with username exists")
        
        email_exists=User.objects.filter(username=attrs['email']).exists()

        if email_exists:
            raise serializers.ValidationError(detail="User with email exists")
        
        phone_number_exists=User.objects.filter(username=attrs['phone_number']).exists()

        if phone_number_exists:
            raise serializers.ValidationError(detail="User with phonenumber exists")


        return super().validate(attrs)

    def create(self, validated_data):

        profile_data = validated_data.pop('profile')
        user = User.objects.create_farmeruser(**validated_data)
        FarmerProfile.objects.create(
            user=user,
            first_name = profile_data['first_name'],
            last_name = profile_data['last_name'],
        )
        return user



class TenderUserCreationSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=25)
    email=serializers.EmailField(max_length=80)
    phone_number=PhoneNumberField(allow_null=False, allow_blank=False)

    profile = TenderSerializer(required=False)

    class Meta:
        model = User
        fields = ('username','email', 'phone_number','password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        username_exists=User.objects.filter(username=attrs['username']).exists()

        if username_exists:
            raise serializers.ValidationError(detail="User with username exists")
        
        email_exists=User.objects.filter(username=attrs['email']).exists()

        if email_exists:
            raise serializers.ValidationError(detail="User with email exists")
        
        phone_number_exists=User.objects.filter(username=attrs['phone_number']).exists()

        if phone_number_exists:
            raise serializers.ValidationError(detail="User with phonenumber  exists")


        return super().validate(attrs)

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_tenderuser(**validated_data)
        TenderProfile.objects.create(
            user=user,
            first_name = profile_data['first_name'],
            last_name = profile_data['last_name'],
        )
        return user


class InputUserCreationSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=25)
    email=serializers.EmailField(max_length=80)
    phone_number=PhoneNumberField(allow_null=False, allow_blank=False)

    profile = InputSerializer(required=False)

    class Meta:
        model = User
        fields = ('username','email', 'phone_number', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        username_exists=User.objects.filter(username=attrs['username']).exists()

        if username_exists:
            raise serializers.ValidationError(detail="User with username exists")
        
        email_exists=User.objects.filter(username=attrs['email']).exists()

        if email_exists:
            raise serializers.ValidationError(detail="User with email exists")
        
        phone_number_exists=User.objects.filter(username=attrs['phone_number']).exists()

        if phone_number_exists:
            raise serializers.ValidationError(detail="User with phonenumber  exists")


        return super().validate(attrs)

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_inputuser(**validated_data)
        InputProfile.objects.create(
            user=user,
            first_name = profile_data['first_name'],
            last_name = profile_data['last_name'],
        )
        return user


class InvestorUserCreationSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=25)
    email=serializers.EmailField(max_length=80)
    phone_number=PhoneNumberField(allow_null=False, allow_blank=False)

    profile = InvestorSerializer(required=False)

    class Meta:
        model = User
        fields = ('username','email', 'phone_number', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        username_exists=User.objects.filter(username=attrs['username']).exists()

        if username_exists:
            raise serializers.ValidationError(detail="User with username exists")
        
        email_exists=User.objects.filter(username=attrs['email']).exists()

        if email_exists:
            raise serializers.ValidationError(detail="User with email exists")
        
        phone_number_exists=User.objects.filter(username=attrs['phone_number']).exists()

        if phone_number_exists:
            raise serializers.ValidationError(detail="User with phonenumber  exists")


        return super().validate(attrs)

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_investoruser(**validated_data)
        InvestorProfile.objects.create(
            user=user,
            first_name = profile_data['first_name'],
            last_name = profile_data['last_name'],
        )
        return user
