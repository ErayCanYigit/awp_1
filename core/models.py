from django.db import models


class AbstractModel(models.Model):
    """Tüm modellerin miras aldığı soyut temel model."""
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name='Güncelleme Tarihi'
    )
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name='Oluşturma Tarihi'
    )

    class Meta:
        abstract = True


class GeneralSetting(AbstractModel):
    """Site genelindeki ayarları key-value şeklinde tutan model."""
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Değişken Adı',
        help_text='Bu ayarın değişken adıdır.',
    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Açıklama',
        help_text='Bu ayarın ne işe yaradığını açıklar.',
    )
    parameter = models.TextField(
        default='',
        blank=True,
        verbose_name='Değer',
        help_text='Bu ayarın değeridir.',
    )

    def __str__(self):
        return f'Genel Ayar: {self.name}'

    class Meta:
        verbose_name = 'Genel Ayar'
        verbose_name_plural = 'Genel Ayarlar'
        ordering = ('name',)


class SkillCategory(AbstractModel):
    """Becerilerin kategorilerini tutan model."""
    name = models.CharField(max_length=100, verbose_name='Kategori Adı')
    icon_class = models.CharField(max_length=100, default='bi bi-gear', verbose_name='İkon Sınıfı', help_text='Örn: bi bi-code-slash')
    order = models.IntegerField(default=0, verbose_name='Sıralama')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Beceri Kategorisi'
        verbose_name_plural = 'Beceri Kategorileri'
        ordering = ('order', 'name',)


class Skill(AbstractModel):
    """Teknik beceri ve yetkinlikleri tutan model."""
    name = models.CharField(max_length=100, verbose_name='Beceri Adı')
    percentage = models.IntegerField(default=0, verbose_name='Yüzde (%)')
    category = models.ForeignKey(
        'SkillCategory',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Kategori'
    )
    order = models.IntegerField(default=0, verbose_name='Sıralama')

    def __str__(self):
        return f'{self.name} - %{self.percentage}'

    class Meta:
        verbose_name = 'Beceri'
        verbose_name_plural = 'Beceriler'
        ordering = ('category', 'order',)


class Experience(AbstractModel):
    """İş deneyimlerini tutan model."""
    company = models.CharField(max_length=200, verbose_name='Şirket')
    position = models.CharField(max_length=200, verbose_name='Pozisyon')
    location = models.CharField(max_length=200, blank=True, default='', verbose_name='Konum')
    start_date = models.CharField(max_length=100, verbose_name='Başlangıç Tarihi')
    end_date = models.CharField(max_length=100, blank=True, default='', verbose_name='Bitiş Tarihi')
    description = models.TextField(blank=True, default='', verbose_name='Açıklama')
    bullet_points = models.TextField(blank=True, default='', verbose_name='Maddeler (her satıra bir madde)')
    image = models.ImageField(upload_to='experience/', blank=True, null=True, verbose_name='Şirket Görseli')
    order = models.IntegerField(default=0, verbose_name='Sıralama')

    def __str__(self):
        return f'{self.company} - {self.position}'

    def get_bullets(self):
        """Madde işaretli metni listeye çevirir."""
        if self.bullet_points:
            return [b.strip() for b in self.bullet_points.split('\n') if b.strip()]
        return []

    class Meta:
        verbose_name = 'İş Deneyimi'
        verbose_name_plural = 'İş Deneyimleri'
        ordering = ('order',)


class Education(AbstractModel):
    """Eğitim bilgilerini tutan model."""
    institution = models.CharField(max_length=200, verbose_name='Kurum')
    degree = models.CharField(max_length=200, verbose_name='Derece')
    field = models.CharField(max_length=200, blank=True, default='', verbose_name='Bölüm')
    location = models.CharField(max_length=200, blank=True, default='', verbose_name='Konum')
    start_date = models.CharField(max_length=100, verbose_name='Başlangıç Tarihi')
    end_date = models.CharField(max_length=100, blank=True, default='', verbose_name='Bitiş Tarihi')
    gpa = models.CharField(max_length=50, blank=True, default='', verbose_name='GNO')
    description = models.TextField(blank=True, default='', verbose_name='Açıklama')
    order = models.IntegerField(default=0, verbose_name='Sıralama')

    def __str__(self):
        return f'{self.institution} - {self.degree}'

    class Meta:
        verbose_name = 'Eğitim'
        verbose_name_plural = 'Eğitimler'
        ordering = ('order',)


class ProjectCategory(AbstractModel):
    """Projelerin kategorilerini tutan model."""
    name = models.CharField(max_length=100, verbose_name='Kategori Adı')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Slug (Url Uyumlu Ad)', help_text='Örn: cloud, web, ai')
    order = models.IntegerField(default=0, verbose_name='Sıralama')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Proje Kategorisi'
        verbose_name_plural = 'Proje Kategorileri'
        ordering = ('order', 'name',)


class Project(AbstractModel):
    """Proje bilgilerini tutan model."""
    title = models.CharField(max_length=200, verbose_name='Proje Başlığı')
    category = models.ForeignKey(
        'ProjectCategory',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Kategori'
    )
    description = models.TextField(blank=True, default='', verbose_name='Açıklama')
    image = models.ImageField(upload_to='projects/', blank=True, null=True, verbose_name='Proje Görseli')
    url = models.URLField(blank=True, default='', verbose_name='Proje Bağlantısı')
    technologies = models.CharField(max_length=500, blank=True, default='', verbose_name='Kullanılan Teknolojiler')
    order = models.IntegerField(default=0, verbose_name='Sıralama')

    def __str__(self):
        return self.title

    def get_tech_list(self):
        """Virgülle ayrılmış teknoloji metnini listeye çevirir."""
        if self.technologies:
            return [t.strip() for t in self.technologies.split(',') if t.strip()]
        return []

    class Meta:
        verbose_name = 'Proje'
        verbose_name_plural = 'Projeler'
        ordering = ('order',)


class Certificate(AbstractModel):
    """Sertifika bilgilerini tutan model."""
    name = models.CharField(max_length=200, verbose_name='Sertifika Adı')
    issuer = models.CharField(max_length=200, verbose_name='Veren Kurum')
    date = models.CharField(max_length=100, blank=True, default='', verbose_name='Tarih')
    description = models.TextField(blank=True, default='', verbose_name='Açıklama')
    order = models.IntegerField(default=0, verbose_name='Sıralama')

    def __str__(self):
        return f'{self.name} - {self.issuer}'

    class Meta:
        verbose_name = 'Sertifika'
        verbose_name_plural = 'Sertifikalar'
        ordering = ('order',)


class SocialLink(AbstractModel):
    """Sosyal medya bağlantılarını tutan model."""
    platform = models.CharField(max_length=100, verbose_name='Platform')
    url = models.URLField(verbose_name='Bağlantı')
    icon_class = models.CharField(max_length=100, verbose_name='İkon CSS Sınıfı',
                                  help_text='Örn: bi bi-github')
    order = models.IntegerField(default=0, verbose_name='Sıralama')

    def __str__(self):
        return self.platform

    class Meta:
        verbose_name = 'Sosyal Medya Bağlantısı'
        verbose_name_plural = 'Sosyal Medya Bağlantıları'
        ordering = ('order',)


class NavbarLink(AbstractModel):
    """Admin panelinden düzenlenebilen dinamik menü elemanlarını tutan model."""
    title = models.CharField(max_length=100, verbose_name='Menü Başlığı')
    url = models.CharField(max_length=200, verbose_name='Hedef URL / Çapa (Anchor)', help_text='Örn: /#about veya /contact/')
    icon_class = models.CharField(max_length=100, verbose_name='İkon Sınıfı (Bootstrap Icons)', help_text='Örn: bi bi-person navicon')
    order = models.IntegerField(default=0, verbose_name='Sıralama Sırası')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Menü Bağlantısı'
        verbose_name_plural = 'Menü Bağlantıları'
        ordering = ('order',)

