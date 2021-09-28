from django.urls import path
from customerapp.views import index, all_customer, detail,add_customer,add,delete_customer,customer_list,customer_detail 
from . import views

urlpatterns = [ 
        path('', views.index), 
        path('all_customer/',views.all_customer),
        path('<int:customer_id>/', views.detail, name='detail'),
        path('add_customer/', views.add_customer),
        path('add/', views.add), 
        path('<int:customer_id>/delete_customer/',views.delete_customer, name='delete_customer'),
        path('customer_api/customers/',views.customer_list),
        path('customer_api/customers/<int:pk>/',views.customer_detail),
]  