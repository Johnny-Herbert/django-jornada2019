from django.contrib import admin
from users.models import User 

class UserAdmin(admin.ModelAdmin):
    #list
    list_display = ('username', 'email', 'is_superuser','create_at') #Diz quais campos voce quer que apareça na listagem
    list_filter = ('is_superuser', 'create_at') #Seta quais tipos de filtragem você pode fazer
    #fields = ['username'] #diz quais campos eu quero que apareça na parte de modificação
    # fieldsets = {
    #     ('Dados do usúario', {
    #         'fields': ('username', 'password', 'email', 'picture'),
    #     }),

    #     ('Permissões usuário', {
    #         'fields': ('is_superuser', 'is_staff', 'groups', 'user_permissions'),
    #     }),
    #     ('Datas', {
    #         'fields': ('date_join', 'last_login'),
    #     }),
    # }
# Register your models here.
admin.site.register(User, UserAdmin)