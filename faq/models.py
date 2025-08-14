from django.db import models

# Create your models here.

class FAQ(models.Model):
    question = models.CharField("سؤال", max_length=255)
    answer = models.TextField("پاسخ")
    is_published = models.BooleanField("منتشر شود؟", default=True)
    order = models.PositiveIntegerField("ترتیب نمایش", default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "سؤال متداول"
        verbose_name_plural = "سؤالات متداول"
        ordering = ["order", "created_at"]

    def __str__(self):
        return self.question