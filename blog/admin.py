from django.contrib import admin
from django.urls import reverse
from blog.models import Post
from django.utils.html import format_html
from django.contrib.auth import get_user_model
User = get_user_model()

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author_link', 'created', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'author']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    autocomplete_fields = ('author',)

    def author_link(self, obj):
        user = obj.author
        link = reverse('admin:auth_user_change', args=[user.pk])
        return format_html('<a href="{}">{}</a>', link, user.get_username())
