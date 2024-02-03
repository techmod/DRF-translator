# from rest_framework import viewsets
# from .models import Translator
# from .serializers import TranslatorSerializer
#
# def sum_values(x, y):
#     return x + y
#
# class TranslatorViewSet(viewsets.ModelViewSet):
#     queryset = Translator.objects.all()
#     serializer_class = TranslatorSerializer
#
#     def perform_create(self, serializer):
#         x = serializer.validated_data['x']
#         y = serializer.validated_data['y']
#         result = sum_values(x, y)
#         serializer.save(result=result)
from rest_framework import viewsets
from .models import Translator
from .serializers import TranslatorSerializer

class TranslatorViewSet(viewsets.ModelViewSet):
    queryset = Translator.objects.all()
    serializer_class = TranslatorSerializer

