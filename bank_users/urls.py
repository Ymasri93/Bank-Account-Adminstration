from django.urls import path

from . import views

urlpatterns = [
    path('', views.BankUserList.as_view(), name='bank_user_list'),
    path('view/<int:pk>', views.BankUserView.as_view(), name='bank_user_view'),
    path('new', views.BankUserCreate.as_view(), name='bank_user_new'),
    path('view/<int:pk>', views.BankUserView.as_view(), name='bank_user_view'),
    path('edit/<int:pk>', views.BankUserUpdate.as_view(), name='bank_user_edit'),
    path('delete/<int:pk>', views.BankUserDelete.as_view(), name='bank_user_delete'),
]
