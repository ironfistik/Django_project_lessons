from django.db import models
from django.db import models


class Vacancy(models.Model):
    STATUS = [
        ("draft", "Черновик"),
        ("open", "Открыта"),
        ("close", "Зактыта")
    ]

    slug = models.SlugField(max_length=50)  # Аналог VARCHAR
    text = models.CharField(max_length=2000)  # Как VARCHAR(200 CHAR)
    status = models.CharField(max_length=6, choices=STATUS, default="draft")
    created = models.DateField(auto_now_add=True)  # Как DATE(sysdate)

    def __str__(self):
        return self.slug
