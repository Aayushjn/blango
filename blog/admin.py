from django.contrib import admin

from blog.models import Comment
from blog.models import Post
from blog.models import Tag

admin.site.register(Tag)


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
