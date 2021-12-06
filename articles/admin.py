from django.contrib import admin
from .models import Article, Comment

# Register your models here.

class CommentINline(admin.TabularInline):
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentINline]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)