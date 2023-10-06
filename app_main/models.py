from django.db import models

# Create your models here.


class HeaderSliderModel(models.Model):
    title = models.CharField(null=True, blank=True, max_length=125)
    promo = models.TextField(null=True, blank=True, max_length=225)
    cta_text = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="button text")
    cta_link = models.URLField(
        null=True, blank=True, verbose_name="button link")
    bg_img = models.ImageField(
        upload_to="Headersliderbg", null=True, verbose_name="background image", help_text="image size: w-1920px x h-1100")
    active = models.BooleanField(default=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Header Slider"
        verbose_name_plural = "Header Sliders"


class ReviewModel(models.Model):
    details = models.TextField(
        null=True, max_length=525, verbose_name="client comment")
    profile = models.ImageField(
        upload_to="client-review-profiles", null=True, blank=True, verbose_name="person image")
    name = models.CharField(max_length=225, null=True,
                            verbose_name="client name")
    position = models.CharField(
        max_length=225, null=True, verbose_name="job description")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}- review"

    class Meta:
        verbose_name = "Client Review"
        verbose_name_plural = "Client Reviews"

        ordering = [
            '-id'
        ]


class ContactInformationModel(models.Model):
    details = models.TextField(
        null=True, blank=True, max_length=325, verbose_name="short summary")
    phone = models.CharField(max_length=122, null=True)
    email = models.CharField(max_length=122, null=True)
    address = models.TextField(null=True, blank=True, max_length=325)
    work = models.TextField(null=True, blank=True,
                            max_length=325, verbose_name="working date & time")

    def __str__(self):
        return f"{self.id}- contact info"

    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Informations"

        ordering = [
            '-id'
        ]


class FooterInformationModel(models.Model):
    details = models.TextField(
        null=True, max_length=325, verbose_name="short summary")
    facebook_link = models.URLField(
        null=True, blank=True, verbose_name="Facebook Link")
    twitter_link = models.URLField(
        null=True, blank=True, verbose_name="Twitter Link")
    instagram_link = models.URLField(
        null=True, blank=True, verbose_name="Instagram Link")
    youtube_link = models.URLField(
        null=True, blank=True, verbose_name="YouTube Link")

    def __str__(self):
        return f"{self.id}- footer info"

    class Meta:
        verbose_name = "Footer Information"
        verbose_name_plural = "Footer Informations"

        ordering = [
            '-id'
        ]


class ProductCategoryModel(models.Model):
    category_name = models.CharField(max_length=225, null=True, blank=True)

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"

    def __str__(self):
        return f"{self.category_name}"


class ProductSubcategoryModel(models.Model):
    category = models.ForeignKey(
        ProductCategoryModel, on_delete=models.CASCADE, null=True)
    sub_category_name = models.CharField(max_length=225, null=True, blank=True)

    class Meta:
        verbose_name = "Product Subcategory"
        verbose_name_plural = "Product Subcategories"

    def __str__(self):
        return f"{self.sub_category_name}"


class ProductModel(models.Model):
    title = models.CharField(max_length=122, null=True,
                             verbose_name="product title")
    category = models.ForeignKey(
        ProductCategoryModel, on_delete=models.CASCADE, null=True, related_name="p_category")
    subcategory = models.ForeignKey(
        ProductSubcategoryModel, on_delete=models.CASCADE, null=True, related_name="p_subcategory")
    details = models.TextField(
        null=True, blank=True, max_length=325, verbose_name="product details")
    info = models.TextField(
        null=True, blank=True, max_length=325, verbose_name="additional information")
    tag = models.CharField(max_length=6, null=True, default="NEW")

    cover_image = models.ImageField(
        upload_to="product-cover-image/%Y/%d/%b", null=True, help_text="image size: w-800px x h-975px")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

        ordering = ["-id"]

    def __str__(self):
        return f"{self.id}: {self.title}"


class ProductImagesModel(models.Model):
    product = models.ForeignKey(
        ProductModel, on_delete=models.CASCADE, null=True)
    image_title = models.CharField(
        max_length=122, null=True, verbose_name="image title")
    image = models.ImageField(upload_to="products-images/%Y/%d/%b", null=True)

    class Meta:
        verbose_name = "Product image"
        verbose_name_plural = "Product images"

    def __str__(self):
        return f"{self.id}: {self.product.title} - {self.image_title}"
