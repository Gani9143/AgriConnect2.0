from django.db import models
from django.conf import settings


class Chatbox(models.Model):
    # Link to your custom Account user model
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sent_messages",
    )
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="received_messages",
    )

    # Optional extra IDs if your logic still uses them
    sp_id = models.IntegerField(null=True, blank=True)
    farmer_id = models.IntegerField(null=True, blank=True)

    text = models.CharField(max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver}"
