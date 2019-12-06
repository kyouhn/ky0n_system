from django.shortcuts import render
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy


class index(LoginRequiredMixin, generic.TemplateView):
    """メニュービュー"""
    template_name = 'accounts/top.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # 継承元のメソッドCALL
        context["form_name"] = "top"
        return context


class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    """パスワード変更ビュー"""
    success_url = reverse_lazy('accounts:password_change_done')
    template_name = 'accounts/password_change.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # 継承元のメソッドCALL
        context["form_name"] = "password_change"
        return context


class PasswordChangeDone(LoginRequiredMixin,PasswordChangeDoneView):
    """パスワード変更完了"""
    template_name = 'accounts/password_change_done.html'