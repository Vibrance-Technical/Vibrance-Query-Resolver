import django_filters 
from . models import Query
class QueryFilter(django_filters.FilterSet):
    slug = django_filters.CharFilter(lookup_expr="iexact",label = "Reference Id")
    date_of_creation = django_filters.DateRangeFilter(label = 'Date')
    class Meta:
        model = Query
        fields = ['status']