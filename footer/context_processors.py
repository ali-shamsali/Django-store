from .models import FooterSettings, FooterCategory

def footer_settings_processor(request):
    footer_settings = FooterSettings.objects.first()
    categories = FooterCategory.objects.prefetch_related('items').all()

    return {
        'footer_settings': footer_settings,
        'footer_categories': categories,
    }
