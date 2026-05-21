from django.test import TestCase, Client
from django.urls import reverse
from core.models import (
    GeneralSetting, SkillCategory, Skill, Experience, Education, 
    ProjectCategory, Project, Certificate, SocialLink, NavbarLink
)

class CoreModelTest(TestCase):
    def setUp(self):
        # Test kategorilerinin oluşturulması
        self.skill_category = SkillCategory.objects.create(
            name="Backend Dilleri",
            icon_class="bi bi-code",
            order=10
        )
        self.project_category = ProjectCategory.objects.create(
            name="Bulut Projeleri",
            slug="cloud",
            order=10
        )

    def test_skill_creation(self):
        """Beceri modelinin oluşturulmasını ve ForeignKey ilişkisini test eder."""
        skill = Skill.objects.create(
            name="Python",
            percentage=90,
            category=self.skill_category,
            order=1
        )
        self.assertEqual(skill.name, "Python")
        self.assertEqual(skill.percentage, 90)
        self.assertEqual(skill.category, self.skill_category)
        self.assertEqual(str(skill), "Python - %90")

    def test_project_creation(self):
        """Proje modelinin oluşturulmasını ve get_tech_list metodunu test eder."""
        project = Project.objects.create(
            title="AWS Dağıtımı",
            category=self.project_category,
            description="AWS bulut testi",
            technologies="Python, Django, AWS",
            order=1
        )
        self.assertEqual(project.title, "AWS Dağıtımı")
        self.assertEqual(project.category, self.project_category)
        self.assertEqual(project.get_tech_list(), ["Python", "Django", "AWS"])
        self.assertEqual(str(project), "AWS Dağıtımı")

    def test_experience_bullets(self):
        """Deneyim maddelerinin split mantığını test eder."""
        exp = Experience.objects.create(
            company="Limon Cloud",
            position="Stajyer",
            bullet_points="Satır 1\nSatır 2\n  Satır 3  ",
            order=1
        )
        self.assertEqual(exp.get_bullets(), ["Satır 1", "Satır 2", "Satır 3"])


class CoreViewTest(TestCase):
    def setUp(self):
        # Arayüz render testleri için gerekli Genel Ayarların ve kayıtların ayarlanması
        GeneralSetting.objects.create(name="site_title", parameter="Eray Can Yiğit | Portfolyo")
        GeneralSetting.objects.create(name="home_banner_name", parameter="Eray Can Yiğit")
        
        self.skill_category = SkillCategory.objects.create(name="Programlama", order=1)
        Skill.objects.create(name="Python", percentage=95, category=self.skill_category)

        self.project_category = ProjectCategory.objects.create(name="Web", slug="web", order=1)
        Project.objects.create(title="E-Ticaret Projesi", category=self.project_category, technologies="Django, React")

    def test_homepage_loads(self):
        """Ana sayfanın başarıyla yüklendiğini ve dinamik verileri içerdiğini test eder."""
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Eray Can Yiğit | Portfolyo")
        self.assertContains(response, "Python")
        self.assertContains(response, "E-Ticaret Projesi")
