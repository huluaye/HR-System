from django.urls import path
from .views import employee_list, employee_add, employee_edit, leave_request_list, leave_request_add

urlpatterns = [
    path('', employee_list, name='employee_list'),
    path('add/', employee_add, name='employee_add'),
    path('edit/<int:pk>/', employee_edit, name='employee_edit'),
    path('leave-requests/', leave_request_list, name='leave_request_list'),
    path('leave-requests/add/', leave_request_add, name='leave_request_add'),
]
