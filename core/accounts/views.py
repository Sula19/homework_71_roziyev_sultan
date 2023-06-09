from django.shortcuts import redirect, reverse
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView
from accounts.forms import LoginForm, CreateUser, UserChangeForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator


class LoginView(TemplateView):
    template_name = 'login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form()
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            return redirect('index')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if not user:
            return redirect('index')
        login(request, user)
        next = request.GET.get('next')
        if next:
            return redirect(next)
        return redirect('index')


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CreateUser

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        context = {'form': form}
        return self.render_to_response(context)

    def get_success_url(self):
        return redirect('/')


class ProfileView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'profile_user.html'
    context_object_name = 'user_obj'
    paginate_related_by = 5
    paginate_related_orphans = 0

    def get_context_data(self, **kwargs):
        posts = self.object.author_post.all()
        paginator = Paginator(posts, self.paginate_related_by, orphans=self.paginate_related_orphans)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        kwargs['page_obj'] = page
        kwargs['posts'] = page.object_list
        kwargs['is_paginated'] = page.has_other_pages()
        return super().get_context_data(**kwargs)


def logout_view(request):
    logout(request)
    return redirect('index')


class UserPasswordChange(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = 'change_password.html'
    form_class = PasswordChangeForm
    context_object_name = 'user_obj'

    def get_success_url(self):
        return reverse('login')


class UserChangeView(LoginRequiredMixin, UpdateView):
    template_name = 'user_change.html'
    model = get_user_model()
    form_class = UserChangeForm
    context_object_name = 'user_obj'

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.kwargs.get('pk')})


class Subscriptions(DetailView):
    template_name = 'subscriptions.html'
    model = get_user_model()
    context_object_name = 'user_sub'


class Subscribers(DetailView):
    template_name = 'subscribers.html'
    model = get_user_model()
    context_object_name = 'user_sub'
