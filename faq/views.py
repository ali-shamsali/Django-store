from django.shortcuts import render
from .models import FAQ

# Create your views here.


def faq_list(request):
    faqs = FAQ.objects.filter(is_published=True).order_by("order", "created_at")
    return render(request, "faq.html", {"faqs": faqs})