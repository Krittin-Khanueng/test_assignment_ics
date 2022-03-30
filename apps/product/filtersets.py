from django.db.models import TextChoices
from django_filters import rest_framework as filters
from .models import Product
from django.core.exceptions import ValidationError


class ProductFilterSet(filters.FilterSet):
    class Meta:
        model = Product
        fields = ['gender', 'category', 'size', 'limit']

    class GenderStateFilters(TextChoices):
        MAN = "MAN", "MAN"
        FEMALE = "FEMALE", "FEMALE"

    gender = filters.CharFilter(method="filter_gender")
    category = filters.CharFilter(method="filter_category")
    size = filters.CharFilter(method="filter_size")
    limit = filters.CharFilter(method="filter_limit")

    def filter_gender(self, queryset, name, value):
        try:
            print(queryset.filter(size__gender='2'))
            if value == ProductFilterSet.GenderStateFilters.MAN:
                return queryset.filter(size__gender='1')
            return queryset.filter(size__gender='2')
        except ValidationError:
            return queryset.none()

    def filter_category(self, queryset, name, value):
        try:
            return queryset.filter(category__name=value)
        except ValidationError:
            return queryset.none()

    def filter_size(self, queryset, name, value):
        try:
            return queryset.filter(size__size__icontains=value)
        except ValidationError:
            return queryset.none()

    def filter_limit(self, queryset, name, value):
        try:
            return queryset.all()[:int(value)]
        except ValidationError:
            return queryset.none()
