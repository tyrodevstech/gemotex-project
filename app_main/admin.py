from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from .models import (
    ProductCategoryModel,
    ProductSubcategoryModel,
    ProductModel,
    ProductImagesModel,
    ContactInformationModel,
    FooterInformationModel,
    HeaderSliderModel,
    ReviewModel,
    BrandGalleryModel,
    PartnerCompanyModel,
    ShortAboutInfoModel,
    IntroVideoModel,
    AboutCardModel,
    AboutVideoModel,
)


# Create an admin class for ProductImagesModel as a tabular inline
class ProductImagesAdmin(admin.TabularInline):
    model = ProductImagesModel
    extra = 1


# Create an admin class for ProductModel
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "subcategory", "tag", "created_at")
    list_filter = ("category", "subcategory", "tag")
    search_fields = ("title", "details")

    # Add the inline for ProductImagesModel
    inlines = [ProductImagesAdmin]

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('load_subcategories/', self.load_subcategories, name='load_subcategories'),
        ]
        return custom_urls + urls
    
    def load_subcategories(self, request):
        category_id = request.GET.get('category_id')
        subcategories = ProductSubcategoryModel.objects.filter(category_id=category_id)
        data = [{'id': subcategory.id, 'name': subcategory.subcategory_name} for subcategory in subcategories]
        return JsonResponse({'subcategories': data})
    
    class Media:
        js = (
            'https://code.jquery.com/jquery-3.6.0.min.js',  # Replace with the appropriate jQuery version
            'js/chained_select.js',  # Create a JavaScript file for chained selects
        )


# Register the ProductModelAdmin
admin.site.register(ProductModel, ProductModelAdmin)


# Create admin classes for other models (if needed)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name",)


class ProductSubcategoryAdmin(admin.ModelAdmin):
    list_display = ("subcategory_name", "category")


class ContactInformationAdmin(admin.ModelAdmin):
    list_display = ("id", "details", "phone", "email", "address", "work")

    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True


class FooterInformationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "details",
        "facebook_link",
        "twitter_link",
        "instagram_link",
        "youtube_link",
    )

    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True


# Register the other models with their respective admin classes
admin.site.register(ProductCategoryModel, ProductCategoryAdmin)
admin.site.register(ProductSubcategoryModel, ProductSubcategoryAdmin)
admin.site.register(ContactInformationModel, ContactInformationAdmin)
admin.site.register(FooterInformationModel, FooterInformationAdmin)


class HeaderSliderAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "active")


admin.site.register(HeaderSliderModel, HeaderSliderAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "created_at")


admin.site.register(ReviewModel, ReviewAdmin)


class BrandGalleryAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "product":
            kwargs["queryset"] = ProductModel.objects.all()  # Replace YourAuthorModel with your actual Author model
            kwargs["empty_label"] = "Select a product"  # Customize the empty label
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(BrandGalleryModel, BrandGalleryAdmin)


class PartnerCompanyAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 6:
            return False
        else:
            return True

admin.site.register(PartnerCompanyModel, PartnerCompanyAdmin)



class ShortAboutInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True

admin.site.register(ShortAboutInfoModel, ShortAboutInfoAdmin)



class IntroVideoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True

admin.site.register(IntroVideoModel, IntroVideoAdmin)


class AboutCardAdmin(admin.ModelAdmin):
    list_display = ("sub_title", "title")

admin.site.register(AboutCardModel, AboutCardAdmin)


class AboutVideoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True

admin.site.register(AboutVideoModel, AboutVideoAdmin)