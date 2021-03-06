from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from customers.models import Customer
from customers.serializers import CustomerSerializer


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
