from app_main.models import (
    ContactInformationModel,
    FooterInformationModel,
    ProductCategoryModel,
)


def miscellaneouscommondata(request):
    contact = ContactInformationModel.objects.all().last()
    footer = FooterInformationModel.objects.all().last()
    categories = ProductCategoryModel.objects.all()

    context = {
        "contact": contact,
        "footer": footer,
        "categories": categories,
    }
    return context
