from django.contrib import admin
from app_main.models import *

# Register your models here.
admin.site.site_header = "GemoTex"


class ContactInformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'email')

    # only create one object
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True


admin.site.register(ContactInformationModel, ContactInformationAdmin)


class FooterInformationAdmin(admin.ModelAdmin):
    # only create one object
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True


admin.site.register(FooterInformationModel, FooterInformationAdmin)


class HeaderSliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'active')


admin.site.register(HeaderSliderModel, HeaderSliderAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'created_at')


admin.site.register(ReviewModel, ReviewAdmin)


admin.site.register(ProductCategoryModel)
admin.site.register(ProductSubcategoryModel)
admin.site.register(ProductModel)
admin.site.register(ProductImagesModel)
