from django.contrib import admin
from core.models import *


@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    """Genel site ayarlarını yöneten admin sınıfı."""
    list_display = ['id', 'name', 'description', 'parameter', 'updated_date', 'created_date']
    search_fields = ['name', 'description', 'parameter']
    list_editable = ['name', 'description', 'parameter']
    list_display_links = ['id']

    class Meta:
        model = GeneralSetting


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'icon_class', 'order']
    list_editable = ['name', 'icon_class', 'order']
    list_display_links = ['id']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """Becerileri yöneten admin sınıfı."""
    list_display = ['id', 'name', 'category', 'percentage', 'order', 'updated_date']
    search_fields = ['name', 'category__name']
    list_editable = ['name', 'category', 'percentage', 'order']
    list_filter = ['category']
    list_display_links = ['id']

    class Meta:
        model = Skill


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    """İş deneyimlerini yöneten admin sınıfı."""
    list_display = ['id', 'company', 'position', 'location', 'start_date', 'end_date', 'order']
    search_fields = ['company', 'position', 'location']
    list_editable = ['company', 'position', 'location', 'start_date', 'end_date', 'order']
    list_display_links = ['id']

    class Meta:
        model = Experience


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    """Eğitim bilgilerini yöneten admin sınıfı."""
    list_display = ['id', 'institution', 'degree', 'field', 'location', 'start_date', 'end_date', 'gpa', 'order']
    search_fields = ['institution', 'degree', 'field']
    list_editable = ['institution', 'degree', 'field', 'location', 'start_date', 'end_date', 'gpa', 'order']
    list_display_links = ['id']

    class Meta:
        model = Education


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'order']
    list_editable = ['name', 'slug', 'order']
    list_display_links = ['id']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Projeleri yöneten admin sınıfı."""
    list_display = ['id', 'title', 'category', 'technologies', 'order']
    search_fields = ['title', 'category__name', 'technologies']
    list_editable = ['title', 'category', 'technologies', 'order']
    list_filter = ['category']
    list_display_links = ['id']

    class Meta:
        model = Project


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    """Sertifikaları yöneten admin sınıfı."""
    list_display = ['id', 'name', 'issuer', 'date', 'order']
    search_fields = ['name', 'issuer']
    list_editable = ['name', 'issuer', 'date', 'order']
    list_display_links = ['id']

    class Meta:
        model = Certificate


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    """Sosyal medya bağlantılarını yöneten admin sınıfı."""
    list_display = ['id', 'platform', 'url', 'icon_class', 'order']
    search_fields = ['platform']
    list_editable = ['platform', 'url', 'icon_class', 'order']
    list_display_links = ['id']

    class Meta:
        model = SocialLink


@admin.register(NavbarLink)
class NavbarLinkAdmin(admin.ModelAdmin):
    """Menü bağlantılarını yöneten admin sınıfı."""
    list_display = ['id', 'title', 'url', 'icon_class', 'order']
    search_fields = ['title', 'url']
    list_editable = ['title', 'url', 'icon_class', 'order']
    list_display_links = ['id']

    class Meta:
        model = NavbarLink

