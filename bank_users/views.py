from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from bank_users.models import BankUser


class BankUserList(ListView):
    model = BankUser


class BankUserView(DetailView):
    model = BankUser


class BankUserCreate(CreateView):
    model = BankUser
    fields = ['first_name', 'last_name', 'iban']
    success_url = reverse_lazy('bank_user_list')


class BankUserUpdate(UpdateView):
    model = BankUser
    fields = ['first_name', 'last_name', 'iban']
    success_url = reverse_lazy('bank_user_list')


class BankUserDelete(DeleteView):
    model = BankUser
    success_url = reverse_lazy('bank_user_list')
