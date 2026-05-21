from django.shortcuts import render
from core.models import GeneralSetting, Skill, Experience, Education, Project, Certificate, SocialLink, SkillCategory, ProjectCategory


def get_general_setting(parameter):
    """Veritabanından genel ayar değerini çeker."""
    try:
        obj = GeneralSetting.objects.get(name=parameter).parameter
    except:
        obj = ''
    return obj


def index(request):
    """Ana sayfa görünümü — tüm veriler veritabanından çekilir."""

    # Genel ayarlar veritabanından çekiliyor
    site_title = get_general_setting('site_title')
    site_keywords = get_general_setting('site_keywords')
    site_description = get_general_setting('site_description')
    home_banner_name = get_general_setting('home_banner_name')
    home_banner_title = get_general_setting('home_banner_title')
    home_banner_description = get_general_setting('home_banner_description')
    about_myself_welcome = get_general_setting('about_myself_welcome')
    about_myself_footer = get_general_setting('about_myself_footer')
    about_birthday = get_general_setting('about_birthday')
    about_phone = get_general_setting('about_phone')
    about_email = get_general_setting('about_email')
    about_city = get_general_setting('about_city')
    about_degree = get_general_setting('about_degree')
    about_university = get_general_setting('about_university')
    typed_items = get_general_setting('typed_items')
    contact_address = get_general_setting('contact_address')
    contact_phone = get_general_setting('contact_phone')
    contact_email = get_general_setting('contact_email')
    hero_subtitle = get_general_setting('hero_subtitle')

    # Veritabanı model sorguları
    skill_categories = SkillCategory.objects.all().prefetch_related('skill_set')
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    projects = Project.objects.all().select_related('category')
    project_categories = ProjectCategory.objects.all()
    certificates = Certificate.objects.all()
    social_links = SocialLink.objects.all()

    context = {
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'home_banner_name': home_banner_name,
        'home_banner_title': home_banner_title,
        'home_banner_description': home_banner_description,
        'about_myself_welcome': about_myself_welcome,
        'about_myself_footer': about_myself_footer,
        'about_birthday': about_birthday,
        'about_phone': about_phone,
        'about_email': about_email,
        'about_city': about_city,
        'about_degree': about_degree,
        'about_university': about_university,
        'typed_items': typed_items,
        'contact_address': contact_address,
        'contact_phone': contact_phone,
        'contact_email': contact_email,
        'hero_subtitle': hero_subtitle,
        'skill_categories': skill_categories,
        'experiences': experiences,
        'educations': educations,
        'projects': projects,
        'project_categories': project_categories,
        'certificates': certificates,
        'social_links': social_links,
    }
    return render(request, 'index.html', context=context)
