from django.urls import path

from . import views

urlpatterns = [
    path('auth/', views.CustomObtainJSONWebToken.as_view(), name='auth'),

]
