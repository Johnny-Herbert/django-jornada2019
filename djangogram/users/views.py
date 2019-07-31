from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from users.forms import UserSignupForm
from users.helpers import send_confirm_user_signup_email
from users.models import User
from users.mixins import UserHasAccessToDetailMixin

#from django.core.email import send_email
# Create your views here.


class UserLoginView(LoginView):
    template_name = 'users/login.html'

class UserLogoutView(LoginRequiredMixin,LogoutView):
    pass

class UserDetailView(generic.DetailView):
    model = User
    contex_object_name = 'user'
    template_name = 'users/detail_user.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request_user = User.objects.get(pk=self.request.user.pk)
        follow_user = kwargs['object']
        context['request_user_has_followed'] = request_user.following.filter(pk=follow_user.pk).exists()
        return context

class UserSignupView(generic.CreateView):
    model = User
    form_class = UserSignupForm
    template_name = 'users/signup_user.html'
    success_url = reverse_lazy('users:login_user')
    def form_valid(self, form):
        #self.object = form.save()
        self.object = form.save(commit=False)
        self.object.save()
        import ipdb; ipdb.set_trace()
        send_confirm_user_signup_email(self.object)
        return super().form_valid(form)

class UserUpdateView(UserHasAccessToDetailMixin,generic.UpdateView):
    model = User
    fields = ['username', 'picture']
    template_name = 'users/update_user.html'
    
    def get_success_url(self):
        return reverse_lazy('users:detail_user', args={self.object.pk})

class UserFollowView(generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        #user logado
        request_user = User.objects.get(pk=self.request.user.pk)
        #user que se quer seguir ou deiar de seguir
        follow_user = User.objects.get(pk=kwargs['pk'])
        #checa se o user logado ja segue o user que esta interagindo
        request_user_has_followed = request_user.following.filter(pk=follow_user.pk).exists()

        if not request_user_has_followed:
            request_user.following.add(follow_user)
            follow_user.followers.add(request_user)
        else:
            request_user.following.remove(follow_user)
            follow_user.followers.remove(request_user)
        return reverse_lazy('users:detail_user', args=[follow_user.pk])