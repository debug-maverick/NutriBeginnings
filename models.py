from django.db import models
from django.urls import reverse


class Progress(models.Model):
    date = models.DateField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    calories = models.PositiveIntegerField(default=0)
    water = models.DecimalField(max_digits=4, decimal_places=1, help_text="Litres")
    steps = models.PositiveIntegerField(default=0)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.date} - {self.weight} kg"


class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    excerpt = models.CharField(max_length=300, blank=True)
    content = models.TextField()
    author = models.CharField(max_length=100, default="Admin")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})
