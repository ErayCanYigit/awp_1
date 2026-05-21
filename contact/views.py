from django.shortcuts import render, redirect
from django.contrib import messages
from contact.models import ContactMessage
from core.models import GeneralSetting, SocialLink


def get_general_setting(parameter):
    """Veritabanından genel ayar değerini çeker."""
    try:
        obj = GeneralSetting.objects.get(name=parameter).parameter
    except:
        obj = ''
    return obj


def contact(request):
    """İletişim sayfası — form gönderimini veritabanına kaydeder."""
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

        if name and email and subject and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message,
            )
            messages.success(request, 'Mesajınız başarıyla gönderildi. Teşekkürler!')
            return redirect('contact')
        else:
            messages.error(request, 'Lütfen tüm alanları doldurunuz.')

    site_title = get_general_setting('site_title')
    home_banner_name = get_general_setting('home_banner_name')
    contact_address = get_general_setting('contact_address')
    contact_phone = get_general_setting('contact_phone')
    contact_email = get_general_setting('contact_email')
    social_links = SocialLink.objects.all()

    context = {
        'site_title': site_title,
        'home_banner_name': home_banner_name,
        'contact_address': contact_address,
        'contact_phone': contact_phone,
        'contact_email': contact_email,
        'social_links': social_links,
    }
    return render(request, 'contact.html', context=context)
