from django.db import models
from django.core.exceptions import ValidationError


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
        ProductCategoryModel,
        on_delete=models.CASCADE,
        null=True,
        related_name="subcategories",
    )
    subcategory_name = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.subcategory_name

    class Meta:
        verbose_name = "Product Subcategory"
        verbose_name_plural = "Product Subcategories"
        unique_together = (("category", "subcategory_name"),)  # Unique constraint

    # def clean(self):
    #     # Custom validation to check uniqueness within the same category
    #     existing_subcategories = ProductSubcategoryModel.objects.filter(
    #         category=self.category,
    #         subcategory_name=self.subcategory_name
    #     )

    #     if self.pk:  # Exclude self when checking for uniqueness during update
    #         existing_subcategories = existing_subcategories.exclude(pk=self.pk)

    #     if existing_subcategories.exists():
    #         raise ValidationError("Subcategory with the same name already exists in this category.")


# Define Product Model
class ProductModel(models.Model):
    title = models.CharField(max_length=122, null=True, verbose_name="Product Title")
    category = models.ForeignKey(
        ProductCategoryModel,
        on_delete=models.CASCADE,
        null=True,
        related_name="products",
    )
    subcategory = models.ForeignKey(
        ProductSubcategoryModel,
        on_delete=models.CASCADE,
        null=True,
        related_name="products",
    )
    details = models.TextField(
        null=True, blank=True, max_length=325, verbose_name="Product Details"
    )
    info = models.TextField(
        null=True, blank=True, max_length=325, verbose_name="Additional Information"
    )
    tag = models.CharField(max_length=6, null=True, default="NEW")

    cover_image = models.ImageField(
        upload_to="product-cover-image/%Y/%d/%b",
        null=True,
        help_text="Size Direction: W:800PX & H:975PX",
    )
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
        ProductModel, on_delete=models.CASCADE, null=True, related_name="images"
    )
    image = models.ImageField(upload_to="products-images/%Y/%d/%b", null=True)

    def __str__(self):
        return f"{self.id} - {self.product.title}"

    class Meta:
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"


# Define Contact Information Model
class HeaderSliderModel(models.Model):
    title = models.CharField(null=True, blank=True, max_length=125)
    promo = models.TextField(null=True, blank=True, max_length=225)
    cta_text = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="button text"
    )
    cta_link = models.URLField(null=True, blank=True, verbose_name="button link")
    bg_img = models.ImageField(
        upload_to="headersliderbg",
        null=True,
        verbose_name="background image",
        help_text="image size: w-1920px x h-1100",
    )
    active = models.BooleanField(default=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Header Slider"
        verbose_name_plural = "Header Sliders"


class ReviewModel(models.Model):
    details = models.TextField(null=True, max_length=525, verbose_name="client comment")
    profile = models.ImageField(
        upload_to="client-review-profiles",
        null=True,
        blank=True,
        verbose_name="person image",
    )
    name = models.CharField(max_length=225, null=True, verbose_name="client name")
    position = models.CharField(
        max_length=225, null=True, verbose_name="job description"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}- review"

    class Meta:
        verbose_name = "Client Review"
        verbose_name_plural = "Client Reviews"

        ordering = ["-id"]


class ContactInformationModel(models.Model):
    details = models.TextField(
        null=True, blank=True, max_length=325, verbose_name="Short Summary"
    )
    phone = models.CharField(max_length=122, null=True)
    email = models.CharField(max_length=122, null=True)
    address = models.TextField(null=True, blank=True, max_length=325)
    work = models.TextField(
        null=True, blank=True, max_length=325, verbose_name="Working Date & Time"
    )

    def __str__(self):
        return f"{self.id} - Contact Info"

    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Informations"
        ordering = ["-id"]


# Define Footer Information Model
class FooterInformationModel(models.Model):
    details = models.TextField(null=True, max_length=325, verbose_name="Short Summary")
    facebook_link = models.URLField(null=True, blank=True, verbose_name="Facebook Link")
    twitter_link = models.URLField(null=True, blank=True, verbose_name="Twitter Link")
    instagram_link = models.URLField(
        null=True, blank=True, verbose_name="Instagram Link"
    )
    youtube_link = models.URLField(null=True, blank=True, verbose_name="YouTube Link")

    def __str__(self):
        return f"{self.id} - Footer Info"

    class Meta:
        verbose_name = "Footer Information"
        verbose_name_plural = "Footer Informations"
        ordering = ["-id"]
