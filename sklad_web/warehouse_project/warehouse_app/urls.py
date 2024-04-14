from django.urls import path
from . import views
from .views import index, add_product,sell_product, edit_sale, SaleListView

urlpatterns = [
    path('', index, name='index'),
    path('add_product/', add_product, name='add_product'),
    path('sell_product/', sell_product, name='sell_product'),
    path('update_payment/<int:sale_id>/', views.update_payment, name='update_payment'),
    path('edit_sale/<int:sale_id>/', edit_sale, name='edit_sale'),
    path('take_money/', views.take_money, name='take_money'),
    path('sale/<str:dokon>/', SaleListView.as_view(), name='sale_list'),
    path('sell/<str:dokon>/', sell_product, name='sell_product_dokon'),
]
