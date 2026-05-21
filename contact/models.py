from django.db import models
from core.models import AbstractModel


class ContactMessage(AbstractModel):
    """Ziyaretçilerden gelen iletişim mesajlarını tutan model."""
    name = models.CharField(max_length=200, verbose_name='Ad Soyad')
    email = models.EmailField(verbose_name='E-posta')
    subject = models.CharField(max_length=300, verbose_name='Konu')
    message = models.TextField(verbose_name='Mesaj')
    is_read = models.BooleanField(default=False, verbose_name='Okundu mu?')

    def __str__(self):
        return f'{self.name} - {self.subject}'

    class Meta:
        verbose_name = 'İletişim Mesajı'
        verbose_name_plural = 'İletişim Mesajları'
        ordering = ('-created_date',)
