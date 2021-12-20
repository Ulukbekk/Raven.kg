from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from orders.views import home_page, order_add, order_detail, order_delete, orders_in_transit, in_transit_list, \
    order_received, received_list, order_pending, pending_list, complete_order, completed_list, order_edit, search

urlpatterns = [
    # path('car-update/<int:pk>/', car_update, name='car_update'),
    path('orders-in-transit/<int:pk>/', orders_in_transit, name='orders_in_transit'),
    path('complete-order/<int:pk>/', complete_order, name='complete_order'),
    path('orders-received/<int:pk>/', order_received, name='order_received'),
    path('orders-pending/<int:pk>/', order_pending, name='order_pending'),
    path('order-delete/<int:pk>/', order_delete, name='order_delete'),
    path('in-transit-list/', in_transit_list, name='in_transit_list'),
    path('completed-list/', completed_list, name='completed_list'),
    path('received-list/', received_list, name='received_list'),
    path('order-edit/<int:pk>/', order_edit, name='order_edit'),
    path('pending-list/', pending_list, name='pending_list'),
    path('order-detail/<int:pk>/', order_detail, name='order_detail'),
    # path('search/', search, name='search'),
    path('order-add/', order_add, name='order_add'),
    path('search', search, name='search'),
    path('', home_page, name='home_page'),
]