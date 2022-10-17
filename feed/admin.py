from django.contrib import admin
from feed import models

# Register your models here.


class PostImageAdmin(admin.StackedInline):
    model = models.PostImage
    extra = 0


class PostAdmin(admin.ModelAdmin):
    model = models.Post
    list_display = (
        'title',
        'user',
        'date_created',
    )
    readonly_fields = ('date_created',)
    inlines = [PostImageAdmin, ]


admin.site.register(models.Post, PostAdmin)