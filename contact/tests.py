from django.test import TestCase, Client
from django.urls import reverse
from contact.models import ContactMessage
from core.models import GeneralSetting

class ContactModelTest(TestCase):
    def test_contact_message_creation(self):
        """İletişim mesajı modelinin oluşturulmasını test eder."""
        msg = ContactMessage.objects.create(
            name="Ahmet Yılmaz",
            email="ahmet@example.com",
            subject="İş Teklifi",
            message="Merhaba, sizinle çalışmak istiyoruz."
        )
        self.assertEqual(msg.name, "Ahmet Yılmaz")
        self.assertEqual(msg.email, "ahmet@example.com")
        self.assertEqual(msg.subject, "İş Teklifi")
        self.assertEqual(msg.message, "Merhaba, sizinle çalışmak istiyoruz.")
        self.assertEqual(str(msg), "Ahmet Yılmaz - İş Teklifi")
        self.assertFalse(msg.is_read)


class ContactViewTest(TestCase):
    def setUp(self):
        # İletişim sayfasının render edilmesi için gerekli Genel Ayarlar
        GeneralSetting.objects.create(name="site_title", parameter="İletişim | Eray Can Yiğit")
        GeneralSetting.objects.create(name="contact_email", parameter="eraycanyigit@example.com")

    def test_contact_page_loads(self):
        """İletişim sayfasının başarıyla render edildiğini doğrular."""
        client = Client()
        response = client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "eraycanyigit@example.com")

    def test_valid_contact_form_submission(self):
        """Geçerli form gönderildiğinde veri tabanına kaydedildiğini ve yönlendirildiğini test eder."""
        client = Client()
        post_data = {
            'name': 'Mehmet Kaya',
            'email': 'mehmet@example.com',
            'subject': 'Soru',
            'message': 'Django projesi hakkında bir sorum var.'
        }
        response = client.post(reverse('contact'), post_data)
        
        # Yönlendirme (redirect) kontrolü
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('contact'))

        # Veritabanında mesajın oluştuğunu teyit etme
        self.assertEqual(ContactMessage.objects.count(), 1)
        msg = ContactMessage.objects.first()
        self.assertEqual(msg.name, 'Mehmet Kaya')

    def test_invalid_contact_form_submission(self):
        """Eksik bilgiyle gönderilen formun kaydedilmediğini doğrular."""
        client = Client()
        # 'message' alanı eksik
        post_data = {
            'name': 'Mehmet Kaya',
            'email': 'mehmet@example.com',
            'subject': 'Soru',
            'message': ''
        }
        response = client.post(reverse('contact'), post_data)
        
        # Yönlendirme yapılmaz, 200 döner ve hata verilir
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactMessage.objects.count(), 0)
