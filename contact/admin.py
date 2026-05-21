from django.contrib import admin
from contact.models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """İletişim mesajlarını yöneten admin sınıfı."""
    list_display = ['id', 'name', 'email', 'subject', 'is_read', 'created_date']
    search_fields = ['name', 'email', 'subject', 'message']
    list_filter = ['is_read', 'created_date']
    list_editable = ['is_read']
    list_display_links = ['id', 'name']

    class Meta:
        model = ContactMessage
