from django.contrib import admin
from posts.models import Post, Comment

class CommentInline(admin.StackedInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    list_filter = ('auth', 'created_at')
    inlines = [CommentInline]


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

admin.site.site_header = "Djangram"
admin.site.index_title = "Admin Djangram"