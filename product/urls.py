from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('detail_product<id>/', views.detailPage, name='detail'),
    path('checkout/', views.checkoutPage, name='checkout'),
    path('cart/', views.cartPage, name='cart'),
    path('add<id>/', views.add_item, name='add_item'),
    path('remove<id>/', views.remove_item, name='remove_item'),
    path('sil<id>/', views.remove_items, name='removes_item'),
    path('process_order/', views.processOrder, name='processOrder'),
    path('filter<id>/', views.categoryList , name="categoryList"),
]
