# from rest_framework import serializers
# from .models import Translator
#
# class TranslatorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Translator
#         fields = ['x', 'y', 'result']
# serializers.py
from rest_framework import serializers
from .models import Translator

def sum_values(x, y):
    return x + y

class TranslatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translator
        fields = ['x', 'y', 'result']
        read_only_fields = ['result']

    def create(self, validated_data):
        x = validated_data['x']
        y = validated_data['y']
        result = sum_values(x, y)
        return Translator.objects.create(x=x, y=y, result=result)


