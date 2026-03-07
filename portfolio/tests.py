from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
# Create your tests here.

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
        
    def test_portfolio_orders_by_updated_at(self):
            first_image = SimpleUploadedFile(
                "first.gif",
                (
                    b"GIF89a\x01\x00\x01\x00\x80\x00\x00"
                    b"\x00\x00\x00\xff\xff\xff!\xf9\x04\x01\x00\x00\x00\x00,"
                    b"\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;"
                ),
                content_type="image/gif",
            )
            second_image = SimpleUploadedFile(
                "second.gif",
                (
                    b"GIF89a\x01\x00\x01\x00\x80\x00\x00"
                    b"\x00\x00\x00\xff\xff\xff!\xf9\x04\x01\x00\x00\x00\x00,"
                    b"\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;"
                ),
                content_type="image/gif",
            )

            first = Project.objects.create(
                title="Proyecto primero",
                description="Descripción primero",
                link="https://example.com/1",
                image=first_image,
            )
            second = Project.objects.create(
                title="Proyecto segundo",
                description="Descripción segundo",
                link="https://example.com/2",
                image=second_image,
            )

            first.description = "Descripción primero actualizada"
            first.save()

            response = self.client.get(reverse("portfolio"))
            projects = list(response.context["projects"])

            self.assertEqual(response.status_code, 200)
            self.assertEqual(projects[0].id, first.id)
            self.assertEqual(projects[1].id, second.id)