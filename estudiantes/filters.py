import django_filters
from .models import *

class AlumnxFilter(django_filters.FilterSet):
    class Meta:
        model = Alumnx
        fields = '__all__'