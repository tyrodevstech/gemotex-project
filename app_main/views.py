from django.shortcuts import render
from django.views.generic import TemplateView

from app_main.models import ContactInformationModel, FooterInformationModel

# Create your views here.


class IndexView(TemplateView):
    template_name = "app_main/index.html"


class AboutView(TemplateView):
    template_name = "app_main/about.html"


class ContactView(TemplateView):
    template_name = "app_main/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact"] = ContactInformationModel.objects.all().last()
        return context


class ProductView(TemplateView):
    template_name = "app_main/product.html"


def custom_page_not_found_view(request, exception=None):
    return render(request, "404.html", {})
