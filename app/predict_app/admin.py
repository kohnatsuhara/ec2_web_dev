from django.contrib import admin
from django.contrib.admin.sites import AdminSite
# Register your models here.
from .models import Post


# class PostAdmin(admin.ModelAdmin):
#     fields = ["author", "title", "text", "created_date", "published_date"]

admin.site.register(Post)



AdminSite.site_header = '管理サイト'
AdminSite.site_title = 'サイト管理者'
AdminSite.index_title = 'サイト管理'
AdminSite.site_url ="/predict_app"