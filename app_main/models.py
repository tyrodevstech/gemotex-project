from django.db import models

# Define Product Category Model
class ProductCategoryModel(models.Model):
    category_name = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"


# Define Product Subcategory Model
class ProductSubcategoryModel(models.Model):
    category = models.ForeignKey(
        ProductCategoryModel, on_delete=models.CASCADE, null=True,related_name='subcategories')
    subcategory_name = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.subcategory_name

    class Meta:
        verbose_name = "Product Subcategory"
        verbose_name_plural = "Product Subcategories"


# Define Product Model
class ProductModel(models.Model):
    title = models.CharField(max_length=122, null=True,
                             verbose_name="Product Title")
    category = models.ForeignKey(
        ProductCategoryModel, on_delete=models.CASCADE, null=True, related_name="products")
    subcategory = models.ForeignKey(
        ProductSubcategoryModel, on_delete=models.CASCADE, null=True, related_name="products")
    details = models.TextField(
        null=True, blank=True, max_length=325, verbose_name="Product Details")
    info = models.TextField(
        null=True, blank=True, max_length=325, verbose_name="Additional Information")
    tag = models.CharField(max_length=6, null=True, default="NEW")

    cover_image = models.ImageField(
        upload_to="product-cover-image/%Y/%d/%b", null=True, help_text="Size Direction: W:800PX & H:975PX")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}: {self.title}"

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["-id"]


# Define Product Images Model
class ProductImagesModel(models.Model):
    product = models.ForeignKey(
        ProductModel, on_delete=models.CASCADE, null=True, related_name="images")
    image = models.ImageField(upload_to="products-images/%Y/%d/%b", null=True)

    def __str__(self):
        return f"{self.id} - {self.product.title}"

    class Meta:
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"


# Define Contact Information Model
class ContactInformationModel(models.Model):
    details = models.TextField(
        null=True, blank=True, max_length=325, verbose_name="Short Summary")
    phone = models.CharField(max_length=122, null=True)
    email = models.CharField(max_length=122, null=True)
    address = models.TextField(null=True, blank=True, max_length=325)
    work = models.TextField(null=True, blank=True,
                            max_length=325, verbose_name="Working Date & Time")

    def __str__(self):
        return f"{self.id} - Contact Info"

    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Informations"
        ordering = ['-id']


# Define Footer Information Model
class FooterInformationModel(models.Model):
    details = models.TextField(
        null=True, max_length=325, verbose_name="Short Summary")
    facebook_link = models.URLField(
        null=True, blank=True, verbose_name="Facebook Link")
    twitter_link = models.URLField(
        null=True, blank=True, verbose_name="Twitter Link")
    instagram_link = models.URLField(
        null=True, blank=True, verbose_name="Instagram Link")
    youtube_link = models.URLField(
        null=True, blank=True, verbose_name="YouTube Link")

    def __str__(self):
        return f"{self.id} - Footer Info"

    class Meta:
        verbose_name = "Footer Information"
        verbose_name_plural = "Footer Informations"
        ordering = ['-id']
