from django.contrib import admin
from .models import Post

# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display=["title","content","updated","timestamp"]
    list_display_links=["updated","timestamp"]
    list_editable=["title"]
    list_filter=["title"]
    search_fields=["title","content"]

    class Meta:
        model=Post

admin.site.register(Post,PostModelAdmin)
