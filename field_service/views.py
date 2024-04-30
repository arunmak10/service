from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'  # Template name for the home page
