# admin.py

from django.contrib import admin
from .models import (
    ProductCategoryModel,
    ProductSubcategoryModel,
    ProductModel,
    ProductImagesModel,
    ContactInformationModel,
    FooterInformationModel,
)

# Create an admin class for ProductImagesModel as a tabular inline
class ProductImagesAdmin(admin.TabularInline):
    model = ProductImagesModel
    extra = 1

# Register the ProductImagesModelAdmin
# Create an admin class for ProductModel
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'subcategory', 'tag', 'created_at')
    list_filter = ('category', 'subcategory', 'tag')
    search_fields = ('title', 'details')
    
    # Add the inline for ProductImagesModel
    inlines = [ProductImagesAdmin]

# Register the ProductModelAdmin
admin.site.register(ProductModel, ProductModelAdmin)

# Create admin classes for other models (if needed)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)

class ProductSubcategoryAdmin(admin.ModelAdmin):
    list_display = ('subcategory_name', 'category')

class ContactInformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'details', 'phone', 'email', 'address', 'work')

class FooterInformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'details', 'facebook_link', 'twitter_link', 'instagram_link', 'youtube_link')

# Register the other models with their respective admin classes
admin.site.register(ProductCategoryModel, ProductCategoryAdmin)
admin.site.register(ProductSubcategoryModel, ProductSubcategoryAdmin)
admin.site.register(ContactInformationModel, ContactInformationAdmin)
admin.site.register(FooterInformationModel, FooterInformationAdmin)
