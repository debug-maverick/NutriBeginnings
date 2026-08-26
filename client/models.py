from django.db import models

# Create your models here.
from Authentication.models import Profile


class Message(models.Model):

    message_id = models.AutoField(
        primary_key=True
    )

    client = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='messages'
    )

    subject = models.CharField(
        max_length=200
    )

    message = models.TextField()

    reply = models.TextField(
        blank=True,
        null=True
    )

    is_replied = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.client.user.username} - {self.subject}"

    class Meta:
        db_table = 'messages'
        ordering = ['-created_at']