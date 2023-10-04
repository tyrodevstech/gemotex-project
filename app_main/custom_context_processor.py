from app_main.models import ContactInformationModel, FooterInformationModel


def miscellaneouscommondata(request):
    contact = ContactInformationModel.objects.all().last()
    footer = FooterInformationModel.objects.all().last()

    context = {
        'contact': contact,
        'footer': footer,
    }
    return context
