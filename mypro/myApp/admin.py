from django.contrib import admin
from .models import Article
from .models import Contact
from .models import Advertisement

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'video')
    search_fields = ('title', 'content')
    list_filter = ('published_date',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    # Mark all fields as read-only
    readonly_fields = ('name', 'email', 'contact_no', 'feedback', 'created_at')

    # Remove the "Add" button
    def has_add_permission(self, request):
        return False

    # Disable editing of existing records
    def has_change_permission(self, request, obj=None):
        return False

    # Disable deletion of records
    def has_delete_permission(self, request, obj=None):
        return False

    # Optionally, display relevant fields in the list view
    list_display = ('name', 'email', 'contact_no', 'feedback', 'created_at')

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'video_url', 'link', 'description')
    search_fields = ('title',)