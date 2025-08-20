from django.shortcuts import render, redirect
from .models import FAQ

# Create your views here.


def faq_submit(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        question = request.POST.get("question")

        if full_name and question:
            FAQ.objects.create(
                full_name=full_name,
                question=question,
                is_published=False
            )
            return redirect(request.path)

    faqs = FAQ.objects.filter(is_published=True).order_by("order", "created_at")
    return render(request, "faq.html", {"faqs": faqs})