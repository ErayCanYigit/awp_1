from core.models import NavbarLink

def navbar_links(request):
    """
    Tüm HTML şablonlarında geçerli olacak dinamik menü bağlantıları bağlam işlemcisi (Context Processor).
    Veri tabanında kayıt yoksa otomatik olarak varsayılan sıralamayı oluşturur.
    """
    try:
        links = list(NavbarLink.objects.all().order_by('order'))
        if not links:
            # Kullanıcının tam olarak istediği yeni sıralama ile varsayılan bağlantılar:
            # 1. Ana Sayfa, 2. Hakkımda, 3. Eğitim, 4. Deneyim, 5. Projeler, 6. Sertifikalar, 7. Beceriler, 8. İletişim
            default_links = [
                ('Ana Sayfa', '/#hero', 'bi bi-house navicon', 10),
                ('Hakkımda', '/#about', 'bi bi-person navicon', 20),
                ('Eğitim', '/#resume', 'bi bi-mortarboard navicon', 30),
                ('Deneyim', '/#experience', 'bi bi-briefcase navicon', 40),
                ('Projeler', '/#portfolio', 'bi bi-images navicon', 50),
                ('Sertifikalar', '/#certificates', 'bi bi-award navicon', 60),
                ('Beceriler', '/#skills', 'bi bi-gear navicon', 70),
                ('İletişim', '/contact/', 'bi bi-envelope navicon', 80),
            ]
            for title, url, icon, order in default_links:
                NavbarLink.objects.create(title=title, url=url, icon_class=icon, order=order)
            links = list(NavbarLink.objects.all().order_by('order'))
        return {'navbar_links': links}
    except Exception:
        # Veri tabanı migrasyonu henüz çalıştırılmadıysa sitenin çökmesini önleyen fallback mekanizması:
        return {
            'navbar_links': [
                {'title': 'Ana Sayfa', 'url': '/#hero', 'icon_class': 'bi bi-house navicon'},
                {'title': 'Hakkımda', 'url': '/#about', 'icon_class': 'bi bi-person navicon'},
                {'title': 'Eğitim', 'url': '/#resume', 'icon_class': 'bi bi-mortarboard navicon'},
                {'title': 'Deneyim', 'url': '/#experience', 'icon_class': 'bi bi-briefcase navicon'},
                {'title': 'Projeler', 'url': '/#portfolio', 'icon_class': 'bi bi-images navicon'},
                {'title': 'Sertifikalar', 'url': '/#certificates', 'icon_class': 'bi bi-award navicon'},
                {'title': 'Beceriler', 'url': '/#skills', 'icon_class': 'bi bi-gear navicon'},
                {'title': 'İletişim', 'url': '/contact/', 'icon_class': 'bi bi-envelope navicon'},
            ]
        }
