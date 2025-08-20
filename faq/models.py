from django.db import models

# Create your models here.

class FAQ(models.Model):
    full_name = models.CharField(
    "نام و نام خانوادگی",
    max_length=150,
    blank=True,
    help_text="برای سوالات ارسالی توسط کاربر"
    )
    question = models.CharField("سؤال", max_length=255)
    answer = models.TextField("پاسخ", blank=True)
    is_published = models.BooleanField("منتشر شود؟", default=False)
    order = models.PositiveIntegerField("ترتیب نمایش", default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "سؤال متداول"
        verbose_name_plural = "سؤالات متداول"
        ordering = ["order", "created_at"]

    def __str__(self):
        return self.question