from rest_framework import serializers

from .models import Information, ElementInformation


class InformationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Information
        #fields = ["id", "viziboll", "name"]
        fields = '__all__'

class ItemInformationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Information
        #fields = ["id", "viziboll"]
        fields = '__all__'

class ElementInformationSerializer(serializers.ModelSerializer):
    information = InformationSerializer(read_only=True, many=False)
    class Meta:
        model = ElementInformation
        #fields = ["id", "viziboll"]
        fields = '__all__'
