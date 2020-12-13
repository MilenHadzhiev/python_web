from django.contrib import admin

from pets.models import Pet, Like, Comment


class LikeInlineAdmin(admin.TabularInline):
    model = Like


class CommentInlineAdmin(admin.TabularInline):
    model = Comment


class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')
    # list_filter = ('type',)
    inlines = [
        LikeInlineAdmin,
        CommentInlineAdmin,
    ]


admin.site.register(Pet, PetAdmin)
admin.site.register(Like)
admin.site.register(Comment)
