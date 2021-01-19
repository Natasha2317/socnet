from django.contrib import admin

# Register your models here.

from mptt.admin import MPTTModelAdmin

from src.wall.models import Post, Comment
from import_export.admin import ImportExportModelAdmin
from src.wall.resources import PostResource, CommentResource
@admin.register(Post)
class PostAdmin(ImportExportModelAdmin):
    """ Посты
    """
    list_display = ("id", "user", "title", "published", "create_date", "moderation", "view_count")
    list_display_links = ["title"]
    list_filter = ["user"]
    search_fields = ['title',]
    resource_class = PostResource



@admin.register(Comment)
class CommentAdmin(ImportExportModelAdmin):
    """ Коментарии к постам
    """
    list_display = ("user", "post", "text", "created_date", "update_date", "published", "id")
    list_display_links = ("text", "post")
    list_filter = ("user", "post")
    search_fields = ['text',]
    mptt_level_indent = 15
    resource_class = CommentResource

