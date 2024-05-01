from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'index.html'  # Template name for the home page
