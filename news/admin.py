from django.contrib import admin
from .models import Post, Comment
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)



class BlogAdmin(admin.ModelAdmin):
    list_display=['author','title','body','created','slug','img']
    prepopulated_fields={'slug':('title',)}