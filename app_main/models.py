from django.db import models

# Create your models here.


class ContactInformation(models.Model):
    details = models.TextField(
        null=True, blank=True, max_length=325, verbose_name="short summary")
    phone = models.CharField(max_length=122, null=True)
    email = models.CharField(max_length=122, null=True)
    adress = models.TextField(null=True, blank=True, max_length=325)
    work = models.TextField(null=True, blank=True,
                            max_length=325, verbose_name="working date & time")

    def __str__(self):
        return f"{self.id}- contact info"

    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Informations"

        ordering = [
            '-id'
        ]
