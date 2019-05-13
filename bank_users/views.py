from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.core.exceptions import PermissionDenied
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from bank_users.forms import BankUserForm
from bank_users.models import BankUser


def has_permission(created_by, request_user):
    return created_by != request_user


class BankUserList(ListView):
    model = BankUser


class BankUserView(DetailView):
    model = BankUser


class BankUserCreate(CreateView):
    model = BankUser
    form_class = BankUserForm
    success_url = reverse_lazy('bank_user_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class BankUserUpdate(UpdateView):
    model = BankUser
    form_class = BankUserForm
    success_url = reverse_lazy('bank_user_list')

    def get_object(self, *args, **kwargs):
        obj = super(BankUserUpdate, self).get_object(*args, **kwargs)
        if obj.created_by == self.request.user:
            raise PermissionDenied()  # or Http404
        return obj


class BankUserDelete(DeleteView):
    model = BankUser
    success_url = reverse_lazy('bank_user_list')

    def get_object(self, *args, **kwargs):
        obj = super(BankUserDelete, self).get_object(*args, **kwargs)
        if obj.created_by == self.request.user:
            raise PermissionDenied()  # or Http404
        return obj
