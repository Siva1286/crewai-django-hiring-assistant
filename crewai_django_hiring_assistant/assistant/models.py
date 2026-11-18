from django.conf import settings
from django.db import models

class HiringGeneration(models.Model):
    EXPERIENCE_CHOICES = [
        ("Entry level", "Entry level"),
        ("1-3 years", "1-3 years"),
        ("3-5 years", "3-5 years"),
        ("5+ years", "5+ years"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="hiring_generations")
    job_title = models.CharField(max_length=160)
    skills = models.TextField()
    experience_level = models.CharField(max_length=40, choices=EXPERIENCE_CHOICES)
    additional_details = models.TextField(blank=True)
    job_description = models.TextField()
    technical_questions = models.TextField()
    hr_questions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.job_title} — {self.user}"
