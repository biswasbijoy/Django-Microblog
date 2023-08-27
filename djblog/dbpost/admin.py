from django.contrib import admin
from dbpost.models.models import Post
from dbpost.models.categories import PostCategory

# admin.site.register(Post)
admin.site.register(PostCategory)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'description', 'published',)
    list_filter = ('user__username', 'title')
    search_fields = ('user__username', 'description', 'title', 'published')
