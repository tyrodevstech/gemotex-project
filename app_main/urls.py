from django.urls import path
from app_main.views import *

app_name = "app_main"


urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("products/", ProductListView.as_view(), name="product_list"),
    path("product/", ProductView.as_view(), name="product"),
    path("contact/", ContactView.as_view(), name="contact"),
]
