from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters.rest_framework import FilterSet, NumberFilter

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['description', 'title']

class ProductFilter(FilterSet):
    products = NumberFilter(field_name='products__id', lookup_expr='contains')
    class Meta:
        model = Stock
        fields = ['address', 'positions', 'products']

class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['products']
    fieldset_class = ProductFilter

