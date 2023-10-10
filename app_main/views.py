from typing import Any
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView

from app_main.models import (
    ContactInformationModel,
    HeaderSliderModel,
    ReviewModel,
    ProductModel,
    ProductSubcategoryModel,
    ProductCategoryModel,
    BrandGalleryModel,
    PartnerCompanyModel,
    ShortAboutInfoModel,
    IntroVideoModel,
    AboutCardModel,
    AboutVideoModel,
    FeaturedProductModel,
    TermsAndConditionsModel,
)

from app_main.utils import send_owner_query_mail, send_client_query_mail, send_owner_contact_mail, send_client_contact_mail
# Create your views here.


class IndexView(TemplateView):
    template_name = "app_main/index.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["featured_products"] = FeaturedProductModel.objects.all()
        context["slider_qs"] = HeaderSliderModel.objects.filter(active=True)
        context["review_qs"] = ReviewModel.objects.all()
        context["brand_gallery_obj"] = BrandGalleryModel.objects.all().first()
        context["partner_company_logos"] = PartnerCompanyModel.objects.all()[:6]
        context["info_obj"] = ShortAboutInfoModel.objects.all().first()
        context["intro_video"] = IntroVideoModel.objects.all().first()
        return context


class AboutView(TemplateView):
    template_name = "app_main/about.html"
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["cards_qs"] = AboutCardModel.objects.all()
        context["about_video_obj"] = AboutVideoModel.objects.first()
        context["terms_qs"] = TermsAndConditionsModel.objects.all()
        return context


class ContactView(TemplateView):
    template_name = "app_main/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact"] = ContactInformationModel.objects.all().last()
        return context
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        client_name = request.POST.get('client_name')
        client_email = request.POST.get('client_email')
        client_message = request.POST.get('client_message')
        send_owner_contact_mail(client_name,client_email,client_message)
        send_client_contact_mail(context['contact'],client_name,client_email,client_message)
        messages.success(request, 'Successfully sent! You can expect to receive an email from the Gemotex team shortly.')
        return self.render_to_response(context)


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

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        client_name = request.POST.get('client_name')
        client_email = request.POST.get('client_email')
        send_owner_query_mail(self.object,client_name,client_email)
        send_client_query_mail(self.object,client_name,client_email)

        messages.success(request, 'Successfully received email!')
        
        return self.render_to_response(context)


def custom_page_not_found_view(request, exception=None):
    return render(request, "404.html", {})
