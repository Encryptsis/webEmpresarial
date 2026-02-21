from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from .models import Project


class PortfolioViewTests(TestCase):
    def test_portfolio_renders_projects(self):
        image = SimpleUploadedFile(
            "test.gif",
            (
                b"GIF89a\x01\x00\x01\x00\x80\x00\x00"
                b"\x00\x00\x00\xff\xff\xff!\xf9\x04\x01\x00\x00\x00\x00,"
                b"\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;"
            ),
            content_type="image/gif",
        )
        Project.objects.create(
            title="Proyecto demo",
            description="Descripción demo",
            link="https://example.com",
            image=image,
        )

        response = self.client.get(reverse("portfolio"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Proyecto demo")
        self.assertContains(response, "Descripción demo")
