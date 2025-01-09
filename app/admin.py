from django.contrib import admin
from .models import Post, CustomUser, Comment, Contact
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(Comment)
