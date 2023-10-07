from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from app_main.models import (
    ContactInformationModel,
    FooterInformationModel,
    ProductModel,
    ProductSubcategoryModel,
    ProductCategoryModel,
)

# Create your views here.


class IndexView(TemplateView):
    template_name = "app_main/index.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["products"] = ProductModel.objects.all()[:4]

        return context


class AboutView(TemplateView):
    template_name = "app_main/about.html"


class ContactView(TemplateView):
    template_name = "app_main/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact"] = ContactInformationModel.objects.all().last()
        return context


class ProductListView(ListView):
    template_name = "app_main/products.html"
    model = ProductModel
    context_object_name = "products"
    paginate_by = 16

    def get_queryset(self):
        # Get the category and subcategory parameters from the URL
        category = self.request.GET.get("category")
        subcategory = self.request.GET.get("subcategory")

        # Filter products based on category and subcategory
        queryset = ProductModel.objects.all()
        if category:
            queryset = queryset.filter(category__category_name=category)
        if subcategory:
            queryset = queryset.filter(subcategory__subcategory_name=subcategory)

        return queryset

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["categories"] = ProductCategoryModel.objects.all()
        context["subcategories"] = (
            ProductSubcategoryModel.objects.order_by()
            .values("subcategory_name")
            .distinct()
        )

        return context


class ProductView(DetailView):
    template_name = "app_main/product.html"
    model = ProductModel
    context_object_name = "product"


def custom_page_not_found_view(request, exception=None):
    return render(request, "404.html", {})
