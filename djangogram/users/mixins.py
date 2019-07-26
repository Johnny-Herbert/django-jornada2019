from django.contrib.auth.mixins import LoginRequiredMixin

class UserHasAccessToDetailMixin(LoginRequiredMixin):
    def handle_no_permission(self):
        messages.error(
            self.request,
            'Você não pode editar um perfil que nao é seu'
        )
        return retirect('users:logout_user')
    def dispatch(self, request, *args, **kwargs):
        user_pk = kwargs.get('pk')
        user = User.objects.get(pk=user.pk)

        if not user == request.user:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)