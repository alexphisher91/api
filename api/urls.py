from argparse import Namespace
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from products.views import ProductView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', ProductView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
