from django.urls import path
from product.views import ProductListView
from product.cache import cached_data_list


urlpatterns = [
    path("list/", ProductListView.as_view()),
    path("cached/", cached_data_list),
]
